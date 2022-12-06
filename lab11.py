from modulos import crc
from modulos import divisionMod2
from modulos import burst_error
import sys
from bitarray import bitarray

def main():
    # Program parameters
    filename = sys.argv[1]
    divisor = bitarray(sys.argv[2])
    crc_len = int(sys.argv[3])
    burst_size = int(sys.argv[4])
    seed = int(sys.argv[5])
    iter_max = int(sys.argv[6])
    # Redundancy
    zero_rem = bitarray(crc_len)
    zero_rem.setall(0)
    counter = 0 # actual number of repetitions
    # Computes CRC
    msg, crc_code = crc.compute(filename, divisor, crc_len)
    print(f'CRC of text file "{filename}" equals {crc_code.to01()}')
    # Evaluation of the CRC robustness
    for i in range(0, iter_max):
        # Burst error generation
        corrupted_msg = burst_error.burst_err(msg + crc_code, burst_size, seed + i)
        # Computes remainder
        rem = divisionMod2.mod2div(bitarray(corrupted_msg), bitarray(divisor))
        # Determines whether rem equals zero or not
        success = 1 if rem[1:len(divisor)] != zero_rem else 0
        # Compute the number of times the CRC detects the error
        counter += success
    print(f'Probabilidad detección/iteración = {counter/iter_max}')

if __name__ == '__main__':
    main()