import numpy as np
from mixmax import MixMaxPRNG
from utils import save_data as save

DEFAULT_MATRIX_SIZE = 128
DEFAULT_SCALE_FACTOR = 1
DEFAULT_OFFSET = 1

N, s, m = DEFAULT_MATRIX_SIZE, DEFAULT_SCALE_FACTOR, DEFAULT_OFFSET
seed = np.random.rand(N)
mixmax = MixMaxPRNG(N, s, m, seed)

# Save floats for TestU01
save.save_floats_for_TestU01(mixmax)
