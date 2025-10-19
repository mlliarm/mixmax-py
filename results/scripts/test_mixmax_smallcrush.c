#include <Python.h>
#include <stdio.h>
#include "unif01.h"
#include "bbattery.h"

// Global Python objects
static PyObject *generator_obj = NULL;
static PyObject *next_method = NULL;

// Function to call Python's mixmax.next()
static double CallPythonNext(void) {
    PyObject *result = PyObject_CallObject(next_method, NULL);
    if (result == NULL) {
        PyErr_Print();
        fprintf(stderr, "Error calling Python next() method\n");
        return 0.0;
    }
    double value = PyFloat_AsDouble(result);
    Py_DECREF(result);
    return value;
}

// TestU01 requires this function for bit generation
static unsigned long ReadBits(void) {
    return (unsigned long)(CallPythonNext() * 4294967296.0);
}

int main(void) {
    unif01_Gen *gen;
    
    printf("Initializing Python interpreter...\n");
    Py_Initialize();
    
    // Add current directory to Python path
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('.')");
    PyRun_SimpleString("sys.path.append('./src')");
    PyRun_SimpleString("sys.path.insert(0, '/home/milia/Documents/dev/python/mixmax-py/src')");
    
    // Import your mixmax module
    printf("Importing MIXMAX module...\n");
    PyObject *module = PyImport_ImportModule("mixmax");
    if (module == NULL) {
        PyErr_Print();
        fprintf(stderr, "Error: Could not import mixmax module\n");
        fprintf(stderr, "Make sure mixmax.py is in current directory or src/\n");
        Py_Finalize();
        return 1;
    }
    
    // Get the MixMaxPRNG class (not Mixmax!)
    PyObject *mixmax_class = PyObject_GetAttrString(module, "MixMaxPRNG");
    if (mixmax_class == NULL) {
        PyErr_Print();
        fprintf(stderr, "Error: Could not find MixMaxPRNG class\n");
        Py_DECREF(module);
        Py_Finalize();
        return 1;
    }
    
    // Create MixMaxPRNG instance: MixMaxPRNG(N=17, s=0)
    printf("Creating MixMaxPRNG generator (N=256, s=-1, m=1)...\n");
    PyObject *args = Py_BuildValue("(iii)", 256, -1, 1);
    generator_obj = PyObject_CallObject(mixmax_class, args);
    Py_DECREF(args);
    
    if (generator_obj == NULL) {
        PyErr_Print();
        fprintf(stderr, "Error: Could not create MixMaxPRNG instance\n");
        Py_DECREF(mixmax_class);
        Py_DECREF(module);
        Py_Finalize();
        return 1;
    }
    
    // Get the next() method
    next_method = PyObject_GetAttrString(generator_obj, "next");
    if (next_method == NULL) {
        PyErr_Print();
        fprintf(stderr, "Error: Could not find next() method\n");
        Py_DECREF(generator_obj);
        Py_DECREF(mixmax_class);
        Py_DECREF(module);
        Py_Finalize();
        return 1;
    }
    
    // Create TestU01 generator wrapper
    printf("Creating TestU01 generator wrapper...\n");
    gen = unif01_CreateExternGenBits("MixMaxPRNG (N=17, s=0)", ReadBits);
    
    // Run SmallCrush battery
    printf("\n");
    printf("========================================\n");
    printf("Running SmallCrush on MixMaxPRNG...\n");
    printf("This will take approximately 5-10 minutes\n");
    printf("========================================\n");
    printf("\n");
    
    bbattery_SmallCrush(gen);
    
    printf("\n");
    printf("========================================\n");
    printf("SmallCrush completed!\n");
    printf("========================================\n");
    
    // Cleanup
    unif01_DeleteExternGenBits(gen);
    Py_DECREF(next_method);
    Py_DECREF(generator_obj);
    Py_DECREF(mixmax_class);
    Py_DECREF(module);
    Py_Finalize();
    
    return 0;
}