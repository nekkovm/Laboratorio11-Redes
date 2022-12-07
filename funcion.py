#---------------------------------------------------------------------------------------------
from bitarray import bitarray
import random
#---------------------------------------------------------------------------------------------
#   Declaracio del burst_error
#---------------------------------------------------------------------------------------------
#   Descripcion de la funcion
#   Esta funcion genera una rafaga de error de longitud n
#   Argumentos:
#   msg         ---> Una matriz de bits que contiene el mensaje que se corrompera
#   burst_siz n ---> La longitud de la rafaga de error
#   seed        ---> Un entero para establecer el RNG (MT19937)
#   Returns     ---> Un mensaje corrupto
def xor(a, b):
    resultado = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            resultado.append('0')
        else:
            resultado.append('1')
    #convertir a str
    return ''.join(resultado)

def mod2_div(divident:bitarray, divisor:bitarray)-> bitarray:
    divident = divident.to01()
    divisor = divisor.to01()
    # Number of bits to be XORed at a time.
    div_longitud = len(divisor)
    # el dividendo debe tener una longitud igual al divisor para poder realizar las operaciones, entonces
    # lo hacemos mas chico
    tmp = divident[0 : div_longitud]
    while div_longitud < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[div_longitud]
        else: 
            #si tenenmos un cero al principio, significa que tenemos que multiplicar por  
            # puros ceros
            tmp = xor('0'*div_longitud, tmp) + divident[div_longitud]
        div_longitud += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*div_longitud, tmp)
    checkword = tmp
    #comprobacion(bitarray(divident),bitarray(checkword),bitarray(divisor))
    return bitarray(checkword)
#---------------------------------------------------------------------------------------------
def burst_error(msg:bitarray,n:int,seed:int)->bitarray:
    if n < len(msg):
        orig_msg = msg.copy()
        #print(f"Original msg: {orig_msg} len: {len(orig_msg)}")
        random.seed(seed)
        inicio = random.randint(0,len(orig_msg)-n)
        #-----------------------------------------------#
        #print(f"Inicio: {inicio}")
        #print(f"Burst error lenght: {n}")
        #-----------------------------------------------#
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
        #-----------------------------------------------#
        #print(f"Corrupted msg: {msg} len: {len(msg)}")
        #-----------------------------------------------#
    else:
        print('Error')
    return bitarray(msg)
#---------------------------------------------------------------------------------------------

msg_int = bitarray('0010')
crc_code = bitarray('101')
suma = msg_int + crc_code
print(suma)
iter_max = 10
burst_siz = 1  # el burst_siz debe de estar en el rango de 0 - longitud de msg + crc_code - 1
seed = 1
counter = 0 # actual number of repetitions

for j in  range(0, iter_max):
    
    c_msg = burst_error(msg_int + crc_code, burst_siz , seed  + j)
    #print('msg: ',c_msg)
    rem = mod2_div(c_msg, crc_code )
    #print('rem: ', rem)
    success = 0 if c_msg != suma else 1
    counter += success 
    #print(counter)

print(f'Probability = {counter/iter_max}')

#---------------------------------------------------------------------------------------------