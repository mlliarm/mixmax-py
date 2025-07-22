def save_floats_for_TestU01(mixmax, N:int=1000000) -> None:
    with open("mixmax_testu01.txt", "w") as f:
        for _ in range(N):
            f.write(f"{mixmax.next():.17f}\n")

def save_bits_for_NIST(mixmax, N:int=1000000) -> None:
    with open("mixmax_nist.txt", "wb") as f:
        byte = 0
        count = 0
        for _ in range(N):
            bit = 1 if mixmax.next() > 0.5 else 0
            byte = (byte << 1) | bit
            count += 1
            if count == 8:
                f.write(bytes([byte]))
                byte = 0
                count = 0
