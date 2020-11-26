# mixmax-py
A python implementation of the MIXMAX PRNG.

## Description
In this project we successfully construct a python implementation of the two-parameter family of C-system operators `A(N,s)`, as discussed in this [1] paper.

## Code
There are two implementations. The first attempt was a naive approach, using vanilla python3 for the construction of the operator `A(N,s)`. The second attempt, which is much better and faster is using cython for speeding up the construction process.

## How to use the python script
To be added soon.

## How to use the cython files

### Building the create_matrix_fast3 module

Simply run in your terminal:

`python3 setup.py build_ext --inplace`

### Using the create_matrix_new.py script
To be added soon.

## Features
Both programs plot the distributions of the eigenvalues of the given `A(N,s)` for input variables `N`,`s` on the plane.

## Results
The results agree with the results presented in the paper [1]. The distribution of the eigenvalues in some cases follow the curve of a cardioid as expected. For various other values of `N` and `s` different shapes are being created. See inside the images directory for more examples.

## Prerequisites

* Python3
* Cython
* Numpy
* Matplotlib

## Thanks
To my friend rembesques.

## References
[1] Konstantin Savvidy, George Savvidy, Spectrum and entropy of C-systems MIXMAX random number
generator, [(DOI)](https://doi.org/10.1016/j.chaos.2016.05.003), [(arxiv)](https://arxiv.org/abs/1510.06274).
