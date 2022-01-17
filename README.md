________________________________________________________________________
mixmax-py - a PRNG based on uniformly hyperbolic Anosov C-systems defined on a torus.

Copyright (C) 2019-2022  Michail Liarmakopoulos <mlliarm@yandex.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
________________________________________________________________________

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

### python 3.6
* cython-0.29.26
* numpy-1.19.5
* matplotlib-3.3.4

## Thanks
To my friend rembesques.

## References
[1] Konstantin Savvidy, George Savvidy, Spectrum and entropy of C-systems MIXMAX random number
generator, [(DOI)](https://doi.org/10.1016/j.chaos.2016.05.003), [(arxiv)](https://arxiv.org/abs/1510.06274).
