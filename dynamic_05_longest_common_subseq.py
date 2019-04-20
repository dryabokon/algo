import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Longest Common Subsequence
def LCS(A1, A2):
	L1 = len(A1)
	L2 = len(A2)

	D = numpy.zeros((L1 + 1, L2 + 1), dtype=numpy.int)
	D[:, 0] = 0
	D[0, :] = 0

	for i1 in range(1,D.shape[0]):
		for i2 in range(1, D.shape[1]):
			if A1[i1 - 1] == A2[i2 - 1]:
				D[i1,i2] = D[i1-1,i2-1]+1
			else:
				D[i1, i2] =max(D[i1 - 1, i2], D[i1, i2 - 1])

	print(D)
	return D[-1, -1]

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	A1 = 'hello'
	A2 = 'halo'

	res = LCS(A1,A2)
	print(res)