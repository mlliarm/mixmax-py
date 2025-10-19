# Dieharder results

## 1. (256, -1, 1)

When run with `(N, s, m) = (256, -1, 1)` to generate 100M numbers in binary format:

```
Running Dieharder test suite on Dieharder_64bit_N256_s-1_m1.bin...
Started at: Sun 19 Oct 2025 03:13:24 PM CEST
15:13:25 #=============================================================================#
15:13:25 #            dieharder version 3.31.1 Copyright 2003 Robert G. Brown          #
15:13:25 #=============================================================================#
15:13:25    rng_name    |           filename             |rands/second|
15:13:25  file_input_raw| Dieharder_64bit_N256_s-1_m1.bin|  5.23e+07  |
15:13:25 #=============================================================================#
15:13:25         test_name   |ntup| tsamples |psamples|  p-value |Assessment
15:13:25 #=============================================================================#
15:13:25    diehard_birthdays|   0|       100|     100|0.00000000|  FAILED  
15:13:31       diehard_operm5|   0|   1000000|     100|0.88428574|  PASSED  
15:13:42 # The file file_input_raw was rewound 1 times
15:13:42   diehard_rank_32x32|   0|     40000|     100|0.00000000|  FAILED  
15:13:44 # The file file_input_raw was rewound 1 times
15:13:44     diehard_rank_6x8|   0|    100000|     100|0.00000000|  FAILED  
15:13:45 # The file file_input_raw was rewound 1 times
15:13:45    diehard_bitstream|   0|   2097152|     100|0.00000000|  FAILED  
15:13:49 # The file file_input_raw was rewound 2 times
15:13:49         diehard_opso|   0|   2097152|     100|0.00000000|  FAILED  
15:13:52 # The file file_input_raw was rewound 3 times
15:13:52         diehard_oqso|   0|   2097152|     100|0.00000000|  FAILED  
15:14:14 # The file file_input_raw was rewound 3 times
15:14:14          diehard_dna|   0|   2097152|     100|0.00000000|  FAILED  
15:14:15 # The file file_input_raw was rewound 3 times
15:14:15 diehard_count_1s_str|   0|    256000|     100|0.00000000|  FAILED  
15:14:17 # The file file_input_raw was rewound 4 times
15:14:17 diehard_count_1s_byt|   0|    256000|     100|0.00000000|  FAILED  
15:14:19 # The file file_input_raw was rewound 4 times
15:14:19  diehard_parking_lot|   0|     12000|     100|0.00000279|   WEAK   
15:14:19 # The file file_input_raw was rewound 4 times
15:14:19     diehard_2dsphere|   2|      8000|     100|0.00530700|  PASSED  
15:14:22 # The file file_input_raw was rewound 4 times
15:14:22     diehard_3dsphere|   3|      4000|     100|0.80171418|  PASSED  
15:14:27 # The file file_input_raw was rewound 5 times
15:14:27      diehard_squeeze|   0|    100000|     100|0.00000000|  FAILED  
15:14:27 # The file file_input_raw was rewound 5 times
15:14:27         diehard_sums|   0|       100|     100|0.33756243|  PASSED  
15:14:27 # The file file_input_raw was rewound 5 times
15:14:27         diehard_runs|   0|    100000|     100|0.66044859|  PASSED  
15:14:27         diehard_runs|   0|    100000|     100|0.82397917|  PASSED  
15:14:32 # The file file_input_raw was rewound 6 times
15:14:32        diehard_craps|   0|    200000|     100|0.81883163|  PASSED  
15:14:32        diehard_craps|   0|    200000|     100|0.43978205|  PASSED  
15:17:19 # The file file_input_raw was rewound 16 times
15:17:19  marsaglia_tsang_gcd|   0|  10000000|     100|0.00000000|  FAILED  
15:17:19  marsaglia_tsang_gcd|   0|  10000000|     100|0.00000000|  FAILED  
15:17:19 # The file file_input_raw was rewound 16 times
15:17:19          sts_monobit|   1|    100000|     100|0.00000000|  FAILED  
15:17:27 # The file file_input_raw was rewound 16 times
15:17:27             sts_runs|   2|    100000|     100|0.00000000|  FAILED  
15:17:38 # The file file_input_raw was rewound 16 times
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:38 
15:17:40 # The file file_input_raw was rewound 16 times
15:17:40 
15:17:43 # The file file_input_raw was rewound 16 times
15:17:43 
15:17:46 # The file file_input_raw was rewound 17 times
15:17:46 
15:17:50 # The file file_input_raw was rewound 17 times
15:17:50 
15:17:55 # The file file_input_raw was rewound 17 times
15:17:55 
15:18:02 # The file file_input_raw was rewound 18 times
15:18:02 
15:18:11 # The file file_input_raw was rewound 19 times
15:18:11 
15:18:22 # The file file_input_raw was rewound 20 times
15:18:22 
15:18:36 # The file file_input_raw was rewound 20 times
15:18:36 
15:18:56 # The file file_input_raw was rewound 21 times
15:18:56 
15:19:25 # The file file_input_raw was rewound 23 times
15:19:25 
15:20:15 # The file file_input_raw was rewound 24 times
15:20:15 
15:20:20 # The file file_input_raw was rewound 24 times
15:20:20 
15:20:27 # The file file_input_raw was rewound 24 times
15:20:27 
15:20:40 # The file file_input_raw was rewound 24 times
15:20:40 
15:21:04 # The file file_input_raw was rewound 24 times
15:21:04 
15:21:05 # The file file_input_raw was rewound 25 times
15:21:05 
15:21:06 # The file file_input_raw was rewound 25 times
15:21:06 
15:21:07 # The file file_input_raw was rewound 25 times
15:21:07 
15:21:10 # The file file_input_raw was rewound 25 times
15:21:10 
15:21:12 # The file file_input_raw was rewound 26 times
15:21:12 
15:21:16 # The file file_input_raw was rewound 27 times
15:21:16 
15:21:21 # The file file_input_raw was rewound 28 times
15:21:21 
15:21:29 # The file file_input_raw was rewound 30 times
15:21:29 
15:21:38 # The file file_input_raw was rewound 33 times
15:21:38 
15:21:49 # The file file_input_raw was rewound 36 times
15:21:49 
15:22:03 # The file file_input_raw was rewound 39 times
15:22:03 
15:22:18 # The file file_input_raw was rewound 43 times
15:22:18 
15:22:36 # The file file_input_raw was rewound 48 times
15:22:36 
15:22:55 # The file file_input_raw was rewound 53 times
15:22:55 
15:23:15 # The file file_input_raw was rewound 58 times
15:23:15 
15:23:38 # The file file_input_raw was rewound 64 times
15:23:38 
15:24:03 # The file file_input_raw was rewound 71 times
15:24:03 
15:24:30 # The file file_input_raw was rewound 78 times
15:24:30 
15:24:58 # The file file_input_raw was rewound 85 times
15:24:58 
15:25:28 # The file file_input_raw was rewound 93 times
15:25:28 
15:25:59 # The file file_input_raw was rewound 102 times
15:25:59 
15:26:33 # The file file_input_raw was rewound 111 times
15:26:33 
15:27:09 # The file file_input_raw was rewound 120 times
```

Obviously we need more numbers.