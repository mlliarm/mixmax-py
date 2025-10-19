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
from numpy.linalg import eig
from typing import List, Tuple
import sys
import matplotlib.pyplot as plt
import math
#from numpy import matrix
from numpy.linalg import inv
from create_matrix_fast3 import create_matrix, create_matrix_three_params


def plot_eigenvalues(eigenvals:list) -> None:
    plt.scatter(eigenvals.real,eigenvals.imag, color= 'red', marker='*')
    #plt.xlim([-1,1])
    #plt.ylim([-1,1])
    plt.show()

def plot_and_save_eigenvalues(eigenvals:list, N:int, s:int, m:int=1) -> None:
    plt.scatter(eigenvals.real,eigenvals.imag, color= 'red', marker='*')
    plt.title("Eigenvalues of matrix with N = {}, s = {}, m = {}".format(N,s,m))
    filename = str(N) + "_" + str(s) + "_" + str(m) + ".png"
    plt.savefig(filename)


def get_inverse_matrix(numpy_matrix:List[List]) -> List[List]:
    # Adding a small value to the diagonal before inversion
    m = 10**(-15)
    numpy_matrix = numpy_matrix + np.eye(numpy_matrix.shape[1])*m
    #return matrix(numpy_matrix, dtype=np.float64).I
    return inv(numpy_matrix)

def entropy(eigenvalues:list) -> float:
    return sum(math.log(abs(x)) for x in eigenvalues if abs(x)>1)

def calculate_entropies(s:int) -> Tuple[List, List]:
    Nvals = list()
    entropies = list()
    for N in range(2,1001,50):
        A = create_matrix(N,s)
        values, _ = eig(get_inverse_matrix(A))
        Nvals.append(N)
        print("Number of index N is: ", N)
        e = entropy(values)
        entropies.append(e)
    return Nvals, entropies

def plot_entropies(entropies:list, Nvals:list) -> None:
    #plt.plot(entropies, marker="*")
    plt.scatter(Nvals, entropies)
    plt.xlabel("Values of N")
    plt.ylabel("Values of Kolmogorov Entropy")
    plt.show()


def calculate_condition_number(numpy_matrix: List[List]) -> float:
    return np.linalg.cond(numpy_matrix)

def has_double_roots(eigenvals:list, N:int) -> bool:
    return not N == len(set(eigenvals))

def print_and_plot_results(inv_A_eigenvals:list, A_eigenvals:list,
    inv_A_eigenvecs:list, A_eigenvecs:list, N:int, s:int, m:int) -> None:
    print("A Eigenvalues:")
    print(A_eigenvals)
    print("-------")
    print("A Eigenvectors:")
    print(A_eigenvecs)
    print("Inverse A Eigenvalues:")
    print(inv_A_eigenvals)
    print("-------")
    print("Inverse A Eigenvectors:")
    print(inv_A_eigenvecs)
    #plot_eigenvalues(inv_A_eigenvals)
    plot_and_save_eigenvalues(inv_A_eigenvals, N, s, m)
    invA_entropy = entropy(inv_A_eigenvals)
    print("Entropy: ",invA_entropy)
    condA = calculate_condition_number(A)
    print("Cond no of A:",condA)
    condInvA = calculate_condition_number(inverse_of_A)
    print("Cond no of inv(A):",condInvA)
    detA = np.linalg.det(A)
    print("Det(A):", detA)
    detInvA = np.linalg.det(inverse_of_A)
    print("Det(inv(A)):", detInvA)
    Adoubleroots = has_double_roots(A_eigenvals, N)
    print("Does A have double roots?", Adoubleroots)
    AInvDoubleroots = has_double_roots(inv_A_eigenvals, N)
    print("Does inv_A have double roots?", AInvDoubleroots)
    # print("Real eigenvals:",inv_A_eigenvals.real)
    # print("Imaginary eigenvals:",inv_A_eigenvals.imag)

    filename = "runinfo_{}_{}_{}.txt".format(N,s,m)
    with open(filename, "w") as file:
        file.write("A Eigenvalues:\n")
        file.write(str(A_eigenvals) + "\n")
        file.write("-------")
        file.write("A Eigenvectors:\n")
        file.write(str(A_eigenvecs) + "\n")
        file.write("Inverse A Eigenvalues:\n")
        file.write(str(inv_A_eigenvals) + "\n")
        file.write("Inverse A Eigenvectors:\n")
        file.write(str(inv_A_eigenvecs) + "\n\n")
        file.write("Entropy: " + str(invA_entropy) + "\n")
        file.write("Cond no of A: " + str(condA) + "\n")
        file.write("Cond no of inv(A): " + str(condInvA) + "\n")
        file.write("Det(A): " +  str(detA) + "\n")
        file.write("Det(inv(A)):" + str(detInvA) + "\n")
        file.write("Does A have double roots?" + str(Adoubleroots) + "\n")
        file.write("Does inv_A have double roots?"+ str(AInvDoubleroots) + "\n\n")
        file.write("Real eigenvals:" + str(inv_A_eigenvals.real) + "\n")
        file.write("Imaginary eigenvals:" + str(inv_A_eigenvals.imag) + "\n")

def keep_real_and_imag_parts_of_eigenvals(eigenvals:list) -> list:
    real_set = set(eigenvals.real)
    imag_set = set(eigenvals.imag)
    result_set = real_set.symmetric_difference(imag_set)
    return list(result_set)

def print_real_and_imag_parts_of_eigenvals(eigenvals:list) -> None:
    real_and_imag_parts_of_eigenvals = keep_real_and_imag_parts_of_eigenvals(eigenvals)
    #real_and_imag_parts_of_eigenvals.sort()
    for real_imag in real_and_imag_parts_of_eigenvals:
        #sys.stdout.write(str(eigen_real)+ '\n')
        print(real_imag)

def write_parts_of_eigenvals_to_disk(eigenvals:list, N:int, s:int, m:int) -> None:
    real_set = set(eigenvals.real)
    imag_set = set(eigenvals.imag)
    with open("real_parts_{}_{}_{}.txt".format(N,s,m), "w") as file:
        for real in real_set:
            file.write(str(real) + "\n")
    with open("imag_parts_{}_{}_{}.txt".format(N,s,m), "w") as file2:
        for imag in imag_set:
            file2.write(str(imag) + "\n")

def print_GPL_msg():
    msg = "mixmax-py Copyright (c) 2019-2022  Michail Liarmakopoulos <mlliarm@yandex.com>\n\
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\n\
    This is free software, and you are welcome to redistribute it\n\
    under certain conditions; type `show c' for details.\n"
    print(msg)


if __name__ == "__main__":
    try:
        #N = 512
        print_GPL_msg()
        N = int(sys.argv[1])
        if N == 0:
            raise ValueError("N should not be zero.")
        #s = -1
        s = int(sys.argv[2])
        m = int(sys.argv[3])
        #m = 2**53 + 1
        # A_three = create_matrix_three_params(N,s,m)
        # A_three = np.array(A_three)
        # print(A_three)
        #if s != 0 and s != -1:
        #    raise ValueError("s should be 0 or -1.")
        print("Creating matrix")
        A = create_matrix_three_params(N,s,m) # A = create_matrix(N,s)
        print("Finished creating matrix")
        A = np.array(A)
        # A = A_three
        print(A)
        #print(A == A_three)
        #A = A_three
        print("Calculating eigenvals, eigenvecs of A")
        A_eigenvals, A_eigenvecs = eig(A)
        print("Finished calculating eigenvals, eigenvecs of A")
        ##print(A)
        print("Inverting A")
        inverse_of_A = get_inverse_matrix(A)
        print("Finished inverting A")
        print("Calculating eigenvals, eigenvecs of inverse A")
        inv_A_eigenvals, inv_A_eigenvecs = eig(inverse_of_A)
        print("Finished calculating eigenvals, eigenvecs of inverse A")
        print("Printing and plotting results")
        print_and_plot_results(inv_A_eigenvals, A_eigenvals, inv_A_eigenvecs, A_eigenvecs, N, s, m)
        print("Finished printing and plotting results")
        print("Writing eigenvals parts to files")
        write_parts_of_eigenvals_to_disk(inv_A_eigenvals, N, s, m)
        print("Finished writing eigenvals parts to files")
        #print_real_and_imag_parts_of_eigenvals(inv_A_eigenvals)
        #vals, entropies = calculate_entropies(s)
        #plot_entropies(entropies, Nvals)
        #print(entropies)
    except Exception as e:
        print(e)
        print("Run as:")
        print("python3 create_matrix.py N s m")
        print()
        print("Where:")
        print("N: size of matrix greater than 1")
        print("s: the magic number, 0 or -1")
        print("m: the third parameter, greater or equal to 1")
        print()
        print("Example:")
        print("python3 create_matrix.py 10 0 1")
