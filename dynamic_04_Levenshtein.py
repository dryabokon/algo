import numpy
# ----------------------------------------------------------------------------------------------------------------------
def levenshtain_distance(A1, A2):

	L1 = len(A1)
	L2 = len(A2)

	D = numpy.zeros((L1+1,L2+1),dtype=numpy.int)
	D[:, 0] = numpy.arange(0, D.shape[0], 1)
	D[0, :] = numpy.arange(0, D.shape[1], 1)

	for i1 in range(1,D.shape[0]):
		for i2 in range(1, D.shape[1]):
			cost = 0 if A1[i1 - 1] == A2[i2 - 1] else 1
			D[i1, i2] = min(1+D[i1,i2-1],1+D[i1-1,i2],cost+D[i1-1,i2-1])

	print(D)
	return D[-1,-1]

# ----------------------------------------------------------------------------------------------------------------------
def levenshtain_distance2(A1,A2):

	D = numpy.zeros((len(A1),len(A2)),dtype=numpy.int)
	D[:, 0] = numpy.arange(0, D.shape[0], 1)
	D[0, :] = numpy.arange(0, D.shape[1], 1)

	for i in range(1,len(A1)):
		for j in range(1,len(A2)):
			cost = 1-1*(A1[i]==A2[j])
			D[i,j] = min(D[i-1][j-1]+cost,1+D[i-1][j],1+D[i][j-1])


	print(D)
	return D[-1,-1]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	A1 = 'catt'
	A2 = 'scatter'

	res = levenshtain_distance(A1,A2)
	print(res)

	res = levenshtain_distance2(A1, A2)
	print(res)

