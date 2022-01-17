##########################################################################################
#
# mixmax-py - a PRNG based on uniformly hyperbolic Anosov C-systems defined on a torus.
#
# Copyright (C) 2019-2022  Michail Liarmakopoulos <mlliarm@yandex.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###########################################################################################

import numpy as np

# DEF N = 1000
# DEF s = 0

def create_matrix(unsigned int N, long s):
    cdef double [:,:] A = np.ones(shape=(N,N),dtype=np.float64)
    cdef int i, j, k
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i-j == k and i > 0 and j > 0:
                    A[i,j] = 2 + k
    if N > 2:
        A[2,1] = 3 + s
    return A

def create_matrix_three_params(unsigned int N, long s, unsigned long m):
    cdef double [:,:] A = np.ones(shape=(N,N),dtype=np.float64)
    cdef int i, j, k
    for i in range(N):
        for j in range(N):
            if i-j == 0 and i > 0 and j > 0:
                A[i,j] = 2
            for k in range(1,N):
                if i-j == k and i > 0 and j > 0:
                    A[i,j] = 2 + k*m
    if N > 2:
        A[2,1] = m + 2 + s
    return A