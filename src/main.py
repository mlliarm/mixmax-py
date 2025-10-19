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
from mixmax import MixMaxPRNG
from utils import save_data as save

DEFAULT_MATRIX_SIZE = 256 #7307
DEFAULT_SCALE_FACTOR = -1 #0
DEFAULT_OFFSET = 1

N, s, m = DEFAULT_MATRIX_SIZE, DEFAULT_SCALE_FACTOR, DEFAULT_OFFSET
seed = np.random.rand(N)
mixmax = MixMaxPRNG(N, s, m, seed)

# Save floats 
#save.save_floats_for_TestU01(mixmax, 10_000_000, "Dieharder_test_N{}_s{}_m{}.txt".format(N,s,m))
# Save bits
save.save_bits_for_NIST(mixmax, 10_000_000, "Dieharder_binary_N{}_s{}_m{}.bin".format(N,s,m))

