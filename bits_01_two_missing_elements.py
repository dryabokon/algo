def find_missing_element(A):

	S1=0
	for each in A:S1^=ord(each)

	S2=0
	for i in range(ord(min(A)),ord(max(A))+1):S2^=i

	return chr(S1^S2)
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list('12345789')

	print(''.join(A))
	res = find_missing_element(A)
	print(res)

