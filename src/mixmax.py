###########################################################################################
#
# mixmax-py - a PRNG based on uniformly hyperbolic Anosov C-systems defined on a torus.
#
# Copyright (C) 2019-2025  Michail Liarmakopoulos <mlliarm@yandex.com>
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
from python.create_matrix1 import create_matrix_three_params as create_matrix
from cython.create_matrix_fast3 import create_matrix_three_params as create_matrix_fast

class MixMaxPRNG:
    """
    A pseudorandom number generator based on the MixMax algorithm.

    The MixMax algorithm generates pseudorandom numbers using matrix multiplication
    and modular arithmetic. It is designed for high performance and long periods.

    Parameters:
        N (int): The size of the state vector and matrix dimensions.
        s (int): A parameter controlling the matrix structure.
        m (int): A parameter influencing the modular arithmetic.
        seed (list[float], optional): Initial state vector. If None, a random state is generated.

    Usage example:
        >>> prng = MixMaxPRNG(N=5, s=3, m=7, seed=[0.1, 0.2, 0.3, 0.4, 0.5])
        >>> random_number = prng.next()
        >>> print(random_number)
    """
    def __init__(self, N, s, m, seed=None):
        self.N = N
        self.s = s
        self.m = m
        #self.A = create_matrix(N,s,m)
        self.A = create_matrix_fast(N,s,m)
        self.state = np.random.rand(N) if seed is None else np.array(seed) % 1.0

    def next(self):
        self.state = np.dot(self.A, self.state) % 1.0
        return self.state[0]
