###########################################################################################
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

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('create_matrix_fast3.pyx'))
