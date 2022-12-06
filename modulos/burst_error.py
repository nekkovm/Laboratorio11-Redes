from bitarray import bitarray
import random

def dec2bin(dec):
    return bin(dec).replace("0b","")

def burst_err(msg:bitarray,n:int,seed:int)->bitarray:
    orig_msg = msg.copy()
    print(f"Original msg: {orig_msg} len: {len(orig_msg)}")
    random.seed(seed)
    n_dec = random.getrandbits(n)
    n_bin = dec2bin(n_dec)
    if(len(n_bin)<n):
        diff = n-len(n_bin)
        n_bin = '0'*diff + n_bin
    print(f"Burst error: {n_bin}")
    print(f"Burst error length: {len(n_bin)} bits")
    msg_len = len(msg)
    first_slice = round((msg_len/3)*1)
    msg[first_slice:(first_slice+n)] = bitarray(n_bin)
    print(f"Corrupted msg: {msg} len: {len(msg)}")
    if len(orig_msg)!=len(msg):
        print("error en la corrupción")
    else:
        print("Mensaje corrompido exitosamente.")
        return bitarray(msg)

if __name__ == '__main__':
    burst_err(bitarray('10101010101010101100101'),5,4)
