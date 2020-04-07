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