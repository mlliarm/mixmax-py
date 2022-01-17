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

#/usr/bin/python3
import subprocess

def run_shit(N, aList):
    "To produce some interesting examples"
    for i in aList:
        subprocess.call(['python3', 'create_matrix_new.py', '{}'.format(N), str(i), str(1)])


if __name__ == "__main__":
    aList = [10000000000000, 20000000000000, 30000000000000, 40000000000000, 50000000000000, 60000000000000, 70000000000000, 80000000000000, 90000000000000, 99999999999999]
    anotherList = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 1234567890, 12345678909, 123456789098, 1234567890987, 12345678909876, 123456789098765, 1234567890987654, 12345678909876543, 123456789098765432, 1234567890987654321]
    run_shit(512, anotherList)
