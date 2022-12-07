from bitarray import bitarray
import random

def burst_err(msg:bitarray,n:int,seed:int)->bitarray:
    orig_msg = msg.copy()
    #print(f"Original msg: {orig_msg} len: {len(orig_msg)}")
    random.seed(seed)
    inicio = random.randint(0,len(orig_msg)-n)
    #print(f"Inicio: {inicio}")
    #print(f"Burst error lenght: {n}")
    if msg[inicio]==1:
        msg[inicio]=0
    else:
        msg[inicio]=1
    for i in range(inicio+1,n+inicio):
        invertir = random.randint(0,1)
        if invertir:
            if msg[i]==0:
                msg[i]=1
            else:
                msg[i]=0
    if msg[n]==0:
        msg[n]=1
    else:
        msg[n]=0
    #print(f"Corrupted msg: {msg} len: {len(msg)}")
    return bitarray(msg)
"""
TEST BENCH
if __name__=='__main__':
    burst_err(bitarray('1111111111'),5,22)
  
    
    
    #sujeto a revisión
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
    ##while(orig_msg.to01()==msg.to01()):
      ##  msg[first_slice:(first_slice+n)] = bitarray(n_bin)
    ##print(f"Corrupted msg: {msg} len: {len(msg)}")
    if len(orig_msg)!=len(msg):
        print("error en la corrupción")
        print("Intentando de nuevo")
        burst_err(orig_msg,n,seed)
    else:
        print("Mensaje corrompido exitosamente.")
        return bitarray(msg)
"""
