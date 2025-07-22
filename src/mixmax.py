import numpy as np
from .create_matrix import create_matrix_three_params as create_matrix

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
        self.A = create_matrix(N,s,m)
        self.state = np.random.rand(N) if seed is None else np.array(seed) % 1.0

    def next(self):
        self.state = np.dot(self.A, self.state) % 1.0
        return self.state[0]
