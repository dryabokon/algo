def find_missing_element(A):

	xor_value=0
	for each in A:
		xor_value^=(each)

	res = (xor_value)

	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = [int(a) for a in list('2345679')]


	res = find_missing_element(A)

	print(res)

