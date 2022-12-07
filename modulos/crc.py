from bitarray import bitarray
from modulos import divisionMod2


def compute(filename: str, divisor: bitarray, len_crc: int) -> tuple[bitarray, bitarray]:
	check_arr = bitarray(len_crc)
	check_arr.setall(0)
	file = open(filename, 'r')
	texto = file.read()
	characters = len(texto)
	print(f"Characters: {characters}")
	#print(f"Texto original: {texto}")
	bin_texto = (''.join(format(ord(x), 'b') for x in texto))
	#print(f"Texto en Bits: {bin_texto}")
	r = len_crc
	bin_texto_redundancia = bin_texto+('0'*r)
	residuo = divisionMod2.mod2div(bitarray(bin_texto_redundancia),divisor)
	check = divisionMod2.mod2div(bitarray(bin_texto)+residuo,divisor)
	print(f"Check: {check}")
	if check.to01() != check_arr.to01():
		print("Error")
	else:
		print(f"CRC: {residuo.to01()}")
		return [bitarray(bin_texto),bitarray(residuo)]