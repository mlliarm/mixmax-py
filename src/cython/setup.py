from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('create_matrix_fast3.pyx'))
