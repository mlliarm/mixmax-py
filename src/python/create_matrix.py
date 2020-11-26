import numpy as np
from numpy.linalg import eig
from typing import List, Tuple
import sys
import matplotlib.pyplot as plt
import math
#from numpy import matrix
from numpy.linalg import inv

def create_matrix(N:int ,s:int) -> List[List]:
    A = np.ones(shape=(N,N),dtype=np.float64)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i-j == k and i > 0 and j > 0:
                    A[i][j] = 2+k
    if N > 2:
        A[2][1] = 3 + s
    return A

def create_matrix_three_params(N:int, s:int, m:int) -> List[List]:
    A = np.ones(shape=(N,N),dtype=np.float64)
    for i in range(N):
        for j in range(N):
            if i-j == 0 and i > 0 and j > 0:
                A[i][j] = 2
            for k in range(1,N):
                if i-j == k and i > 0 and j > 0:
                    A[i][j] = 2 + k*m
    if N > 2:
        A[2][1] = m + 2 + s
    return A

def plot_eigenvalues(eigenvals:list) -> None:
    plt.scatter(eigenvals.real,eigenvals.imag, color= 'red', marker='*')
    #plt.xlim([-1,1])
    #plt.ylim([-1,1])
    plt.show()

def plot_and_save_eigenvalues(eigenvals:list, N:int, s:int, m:int=1) -> None:
    plt.scatter(eigenvals.real,eigenvals.imag, color= 'red', marker='*')
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

if __name__ == "__main__":
    try:
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
        A = create_matrix(N,s)
        #A = A_three
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
        print("m: another magic number greater or equal than zero")
        print()
        print("Example:")
        print("python3 create_matrix.py 10 0 0")
