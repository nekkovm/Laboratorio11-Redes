from modulos import crc
from modulos import divisionMod2
from bitarray import bitarray
#CRC-6 1000011
#alt 110011

msg,crc_code = crc.compute("hola.txt",bitarray('1000011'),5)
print(f'CRC of text file "hola.txt" equals {crc_code.to01()}')
"""
TEST BENCH
residuo = divisionMod2.mod2div(bitarray('1110010101000'),bitarray('1101'))
print(f"CRC:{residuo}")
"""