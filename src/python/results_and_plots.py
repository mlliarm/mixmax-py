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

import numpy as np
from numpy.linalg import eig
from typing import List, Tuple
import sys
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv
from create_matrix1 import create_matrix, create_matrix_three_params

def plot_eigenvalues(eigenvals:list) -> None:
    """
    Plot eigenvalues in the complex plane.

    Parameters:
        eigenvals (list): A list or array of complex eigenvalues.

    Display:
        - Eigenvalues are plotted as red stars in the complex plane.
        - Real parts on x-axis, imaginary parts on y-axis.
        - The plot is displayed interactively.

    Note:
        This function is useful for visualizing the spectral properties of matrices.
    """
    plt.scatter(eigenvals.real,eigenvals.imag, color= 'red', marker='*')
    #plt.xlim([-1,1])
    #plt.ylim([-1,1])
    plt.show()

def plot_and_save_eigenvalues(eigenvals:list, N:int, s:int, m:int=1) -> None:
    """
    Plot eigenvalues in the complex plane and save to a file.

    Parameters:
        eigenvals (list): A list or array of complex eigenvalues.
        N (int): Matrix size parameter (used in filename).
        s (int): Magic number parameter (used in filename).
        m (int): Third parameter (used in filename). Defaults to 1.

    Output:
        - Saves a PNG file named "{N}_{s}_{m}.png" with the eigenvalue plot.
        - Eigenvalues are plotted as red stars in the complex plane.

    Note:
        The filename encodes the matrix parameters for easy identification.
    """
    plt.scatter(eigenvals.real,eigenvals.imag, color= 'red', marker='*')
    filename = str(N) + "_" + str(s) + "_" + str(m) + ".png"
    plt.savefig(filename)


def get_inverse_matrix(numpy_matrix:List[List]) -> List[List]:
    """
    Calculate the inverse of a matrix with numerical stabilization.

    Parameters:
        numpy_matrix (List[List]): A square numpy matrix.

    Returns:
        List[List]: The inverse of the input matrix.

    Numerical stabilization:
        - Adds a small value (10^-15) to the diagonal to improve numerical stability.
        - Uses numpy's inv() function for matrix inversion.

    Note:
        The diagonal perturbation helps avoid singularity issues in nearly singular matrices.
    """
    # Adding a small value to the diagonal before inversion
    m = 10**(-15)
    numpy_matrix = numpy_matrix + np.eye(numpy_matrix.shape[1])*m
    #return matrix(numpy_matrix, dtype=np.float64).I
    return inv(numpy_matrix)

def entropy(eigenvalues:list) -> float:
    """
    Calculate the Anosov automorphism entropy from eigenvalues.

    Parameters:
        eigenvalues (list): A list or array of complex eigenvalues.

    Returns:
        float: The Anosov automorphism entropy value.

    Calculation:
        - Sums log(|λ|) for all eigenvalues λ where |λ| > 1 (see Savvidi et al ref. eq. 1.3, 1.4)
        - This measures the exponential rate of divergence in dynamical systems.
    """
    return sum(math.log(abs(x)) for x in eigenvalues if abs(x)>1)

def calculate_entropies(s:int) -> Tuple[List, List]:
    """
    Calculate Anosov automorphism entropies for a range of matrix sizes.

    Parameters:
        s (int): The magic number parameter for matrix creation.

    Returns:
        Tuple[List, List]: A tuple containing:
            - List of N values (matrix sizes from 2 to 1000 in steps of 50).
            - List of corresponding entropy values.

    Process:
        - Creates matrices for N = 2, 52, 102, ..., 952.
        - Computes eigenvalues of the inverse matrix.
        - Calculates Anosov automorphism entropy for each size.
    """
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
    """
    Plot Anosov automorphisms entropies versus matrix size.

    Parameters:
        entropies (list): List of entropy values.
        Nvals (list): List of corresponding N (matrix size) values.

    Display:
        - Scatter plot with N values on x-axis and entropy on y-axis.
        - Shows how entropy changes with matrix size.
        - Plot is displayed interactively.
    """
    #plt.plot(entropies, marker="*")
    plt.scatter(Nvals, entropies)
    plt.xlabel("Values of N")
    plt.ylabel("Values of Anosov Automorphism Entropy")
    plt.show()


def calculate_condition_number(numpy_matrix: List[List]) -> float:
    """
    Calculate the condition number of a matrix.

    Parameters:
        numpy_matrix (List[List]): A square numpy matrix.

    Returns:
        float: The condition number of the matrix.

    Interpretation:
        - Measures how sensitive the matrix inverse is to perturbations.
        - Higher values indicate numerical instability.
        - A condition number near 1 indicates a well-conditioned matrix.

    Note:
        Useful for assessing numerical stability of matrix operations.
    """
    return np.linalg.cond(numpy_matrix)

def has_double_roots(eigenvals:list, N:int) -> bool:
    """
    Check if a matrix has repeated eigenvalues.

    Parameters:
        eigenvals (list): List or array of eigenvalues.
        N (int): Expected number of distinct eigenvalues (matrix size).

    Returns:
        bool: True if there are repeated eigenvalues, False otherwise.

    Method:
        - Compares the number of unique eigenvalues to the expected count N.
        - Uses set conversion to eliminate duplicates.

    Note:
        Repeated eigenvalues can indicate special symmetries or degeneracies.
    """
    return not N == len(set(eigenvals))

def print_and_plot_results(inv_A_eigenvals:list, A_eigenvals:list,
    inv_A_eigenvecs:list, A_eigenvecs:list, N:int, s:int, m:int) -> None:
    """
    Print comprehensive analysis results and plot eigenvalues.

    Parameters:
        inv_A_eigenvals (list): Eigenvalues of the inverse matrix.
        A_eigenvals (list): Eigenvalues of the original matrix.
        inv_A_eigenvecs (list): Eigenvectors of the inverse matrix.
        A_eigenvecs (list): Eigenvectors of the original matrix.
        N (int): Matrix size parameter.
        s (int): Magic number parameter.
        m (int): Third parameter.

    Output:
        - Prints eigenvalues and eigenvectors of both A and inv(A).
        - Displays eigenvalue plots.
        - Saves eigenvalue plot to file.
        - Prints Anosov automorphism entropy, condition numbers, determinants.
        - Checks for repeated eigenvalues.
        - Displays real and imaginary parts of eigenvalues.
    """
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
    plot_eigenvalues(inv_A_eigenvals)
    plot_and_save_eigenvalues(inv_A_eigenvals, N, s, m)
    print(entropy(inv_A_eigenvals))
    print("Cond no of A:",calculate_condition_number(A))
    print("Cond no of inv(A):",calculate_condition_number(inverse_of_A))
    print("Det(A):", np.linalg.det(A))
    print("Det(inv(A)):", np.linalg.det(inverse_of_A))
    print("Does A have double roots?", has_double_roots(A_eigenvals, N))
    print("Does inv_A have double roots?", has_double_roots(inv_A_eigenvals, N))
    print("Real eigenvals:",inv_A_eigenvals.real)
    print("Imaginary eigenvals:",inv_A_eigenvals.imag)

def keep_real_and_imag_parts_of_eigenvals(eigenvals:list) -> list:
    """
    Extract unique real and imaginary parts from eigenvalues.

    Parameters:
        eigenvals (list): List or array of complex eigenvalues.

    Returns:
        list: A list containing the symmetric difference of real and imaginary parts.

    Method:
        - Extracts all real parts into a set.
        - Extracts all imaginary parts into a set.
        - Returns the symmetric difference (elements in one set but not both).

    Note:
        Useful for identifying distinct numerical values in eigenvalue spectra.
    """
    real_set = set(eigenvals.real)
    imag_set = set(eigenvals.imag)
    result_set = real_set.symmetric_difference(imag_set)
    return list(result_set)

def print_real_and_imag_parts_of_eigenvals(eigenvals:list) -> None:
    """
    Print unique real and imaginary parts of eigenvalues.

    Parameters:
        eigenvals (list): List or array of complex eigenvalues.

    Output:
        - Prints each unique real or imaginary part on a separate line.
        - Uses keep_real_and_imag_parts_of_eigenvals() to extract values.

    Note:
        Provides a compact view of the numerical values in the eigenvalue spectrum.
    """
    real_and_imag_parts_of_eigenvals = keep_real_and_imag_parts_of_eigenvals(eigenvals)
    #real_and_imag_parts_of_eigenvals.sort()
    for real_imag in real_and_imag_parts_of_eigenvals:
        #sys.stdout.write(str(eigen_real)+ '\n')
        print(real_imag)

def print_GPL_msg():
    """
    Print the GPL license notice and warranty disclaimer.

    Output:
        - Displays copyright information.
        - Shows GPL license notice.
        - Includes warranty disclaimer.
        - Mentions redistribution conditions.
    """
    msg = "mixmax-py Copyright (c) 2019-2022  Michail Liarmakopoulos <mlliarm@yandex.com>\n\
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\n\
    This is free software, and you are welcome to redistribute it\n\
    under certain conditions; type `show c' for details.\n"
    print(msg)

if __name__ == "__main__":
    try:
        print_GPL_msg()
        #N = 512
        N = int(sys.argv[1])
        if N == 0:
            raise ValueError("N should not be zero.")
        #s = -1
        s = int(sys.argv[2])
        m = int(sys.argv[3])
        #m = 2**53 + 1

        A_three = create_matrix_three_params(N,s,m)
        print(A_three)
        #if s != 0 and s != -1:
        #    raise ValueError("s should be 0 or -1.")
        #A = create_matrix(N,s)
        A = A_three
        print(A)
        #print(A == A_three)
        ##A = A_three
        A_eigenvals, A_eigenvecs = eig(A)
        ##print(A)
        inverse_of_A = get_inverse_matrix(A)
        inv_A_eigenvals, inv_A_eigenvecs = eig(inverse_of_A)
        print_and_plot_results(inv_A_eigenvals, A_eigenvals, inv_A_eigenvecs, A_eigenvecs, N, s, m)
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
        print("python3 create_matrix.py 10 0 0")
