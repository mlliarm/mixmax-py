import numpy as np
from python.create_matrix import create_matrix_three_params as create_matrix

class MixMaxPRNG:
    def __init__(self, N, s, m, seed=None):
        self.N = N
        self.s = s
        self.m = m
        self.A = create_matrix(N,s,m)
        self.state = np.random.rand(N) if seed is None else np.array(seed) % 1.0

    def next(self):
        self.state = np.dot(self.A, self.state) % 1.0
        return self.state[0]
