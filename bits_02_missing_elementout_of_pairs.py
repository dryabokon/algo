# Find two non-repeating elements in an array of repeating elements
# ----------------------------------------------------------------------------------------------------------------------
def find_two_non_rep(A):
	xor_value=0
	value1,value2 = 0,0

	for each in A:
		xor_value^=ord(each)

	rightmost_bit_mask = xor_value & (~(xor_value-1))

	for each in A:
		if ord(each)&rightmost_bit_mask == rightmost_bit_mask:
			value1 ^= ord(each)
		else:
			value2 ^= ord(each)

	return [chr(value1),chr(value2)]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list('2288446677141409aann')

	print(''.join(A))
	res = find_two_non_rep(A)
	print(res)