import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Longest Increasive Subsequence
def LIS(A):
	L = len(A)
	D = numpy.full(L, 1)
	I = numpy.full(L,-1)

	for i in range(1, L):
		for j in range (0, i):
			if A[j]<=A[i]:
				D[i]=D[j]+1
				I[i]=j

	print(' '.join(A))
	print(D)
	i = numpy.argmax(D)
	res=[]
	while i>=0:
		res.append(A[i])
		i=I[i]

	res = [res[len(res)-1-i] for i in range(len(res))]
	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	A = numpy.array(list('12233423454345'))

	res = LIS(A)

	print(' '.join(res))