# mixmax-py
A python implementation of the MIXMAX PRNG.

## Description
In this project we successfully construct a python implementation of the two-parameter family of C-system operators `A(N,s)`, as discussed in this [1] paper. A more general three-parameter family of C-system operators `A(N,s,m)` is calculated too. But our generator doesn't produce all the results of the three parameter family, whereas it works good for the two parameter family. 

## Code
There are two implementations. The first attempt was a naive approach, using vanilla python3 for the construction of the operator `A(N,s)`. The second attempt, which is much better and faster is using cython for speeding up the construction process.

## How to use the python script
Run: `python3 create_matrix.py` . You'll get instructions then.

An example of correct run: `python3 create_matrix.py 128 1 1`. 

## How to use the cython files

### Building the create_matrix_fast3 module

Simply run in your terminal:

`python3 setup.py build_ext --inplace`

### Using the create_matrix_new.py script
Run: `python3 create_matrix_new.py`. You'll get instructions then.

A correct run: `python3 create_matrix_new.py 128 1 1`.

## Features
Both programs plot the distributions of the eigenvalues of the given `A(N,s,m)` for input variables `N,s,m` on the plane.
When `m` equals `1` then `A(N,s,m)` is the same matrix as the matrix `A(N,s)`.

## Results
The results agree with the results presented in the paper [1]. The distribution of the eigenvalues in some cases follow the curve of a cardioid as expected. For various other values of `N` and `s` different shapes are being created. See inside the images directory for more examples.

## Dependencies

* Python3
* Cython
* Numpy
* Matplotlib

## Thanks
To my friend rembesques.

## References
[1] Konstantin Savvidy, George Savvidy, Spectrum and entropy of C-systems MIXMAX random number
generator, [(DOI)](https://doi.org/10.1016/j.chaos.2016.05.003), [(arxiv)](https://arxiv.org/abs/1510.06274).
