import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Longest Common Subsequence
# ----------------------------------------------------------------------------------------------------------------------
def LCS2(A1, A2):

	D = numpy.zeros((len(A1), len(A2)), dtype=numpy.int)
	D[:, 0] = numpy.array([1*(A2[0]==a) for a in A1])
	D[0, :] = numpy.array([1*(A1[0]==a) for a in A2])
	for i1 in range(1,D.shape[0]):
		for i2 in range(1, D.shape[1]):
			if A1[i1]==A2[i2]:
				D[i1, i2]=D[i1-1, i2-1]+1

	i,j = numpy.unravel_index(numpy.argmax(D),D.shape)
	L = D[i,j]
	res = A1[i-L+1:i+1]
	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	A1 = 'hello kitti'
	A2 = 'sdaa'

	res = LCS2(A1,A2)
	print(res)