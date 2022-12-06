from bitarray import bitarray
from modulos import divisionMod2


def compute(filename: str, divisor: str, len_crc: int) -> tuple[bitarray, bitarray]:
	file = open(filename, 'r')
	texto = file.read()
	print(f"Texto original: {texto}")
	bin_texto = (''.join(format(ord(x), 'b') for x in texto))
	print(f"Texto en Bits: {bin_texto}")
	r = len_crc
	bin_texto_redundancia = bin_texto+('0'*r)
	residuo = divisionMod2.mod2div(bitarray(bin_texto_redundancia),divisor)
	print(f"CRC: {residuo.to01()}")
	return [bitarray(bin_texto),bitarray(residuo)]