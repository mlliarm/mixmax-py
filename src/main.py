import numpy as np
from mixmax import MixMaxPRNG
from utils import save_data as save

N, s, m = 128, 1, 1 #5, 1, 0
seed = np.random.rand(N)
mixmax = MixMaxPRNG(N,s,m,seed)

# Save floats for TestU01
save.save_floats_for_TestU01(mixmax)
