def create_matrix(N:int ,s:int) -> List[List]:
    """
    Create an N x N matrix with specific structure for the MIXMAX generator.

    Parameters:
        N (int): The size of the square matrix (must be greater than 1).
        s (int): The magic number parameter (typically 0 or -1).

    Returns:
        List[List]: An N x N numpy array with float64 dtype.

    Matrix structure:
        - All elements are initially set to 1.
        - Diagonal and super-diagonal elements follow the pattern: A[i][j] = 2+k where k = i-j.
        - If N > 2, the element A[2][1] is set to 3 + s.

    Note:
        This function creates the characteristic matrix used in MIXMAX PRNG algorithms.
    """
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
    """
    Create an N x N matrix with three parameters for the MIXMAX generator.

    Parameters:
        N (int): The size of the square matrix (must be greater than 1).
        s (int): The magic number parameter (typically 0 or -1).
        m (int): The third parameter controlling diagonal scaling (must be >= 1).

    Returns:
        List[List]: An N x N numpy array with float64 dtype.

    Matrix structure:
        - All elements are initially set to 1.
        - Diagonal elements (i=j, i>0): A[i][j] = 2.
        - Off-diagonal elements where i-j=k: A[i][j] = 2 + k*m.
        - If N > 2, the element A[2][1] is set to m + 2 + s.

    Note:
        This is an extended version of create_matrix with an additional parameter m.
    """
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