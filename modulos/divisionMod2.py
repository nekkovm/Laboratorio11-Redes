from bitarray import bitarray

def xor(a, b):
    resultado = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            resultado.append('0')
        else:
            resultado.append('1')
    #convertir a str
    return ''.join(resultado)

def mod2div(divident:bitarray, divisor:bitarray)-> bitarray:
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

#TEST BENCH
"""
if __name__=='__main__':
    rem = mod2div(bitarray('100010110101101001110'),bitarray('1001'))
    check = mod2div(bitarray('100010110101101001110')+rem,bitarray('1001'))
    print(f"rem:{rem}")
    print(f"check: {check}")
"""