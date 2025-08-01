def save_floats_for_TestU01(mixmax, N:int=1000000, filename:str="mixmax_testu01.txt") -> None:
    with open(filename, "w") as f:
        for _ in range(N):
            f.write(f"{mixmax.next():.17f}\n")

def save_bits_for_NIST(mixmax, N:int=1000000, filename:str="mixmax_nist.txt") -> None:
    """
    Save binary data generated by the `mixmax` generator in a format suitable for the NIST testing suite.

    Parameters:
        mixmax: An object with a `next()` method that generates floating-point numbers in the range [0, 1).
        N (int): The number of bits to generate. Defaults to 1,000,000.
        filename (str): The name of the file to save the binary data. Defaults to "mixmax_nist.txt".

    Binary format:
        - Each bit is determined by whether the output of `mixmax.next()` is greater than 0.5 (1 for True, 0 for False).
        - Bits are grouped into bytes (8 bits per byte) and written to the specified file.

    Note:
        Ensure that the `mixmax` generator is properly initialized before calling this function.
    """
    with open(filename, "wb") as f:
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
        # Write the last incomplete byte if there are remaining bits
        if count > 0:
            byte = byte << (8 - count)  # Shift remaining bits to fill the byte
            f.write(bytes([byte]))
