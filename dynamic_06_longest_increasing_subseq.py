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
				if (D[j]+1>D[i]):
					D[i]=D[j]+1
					I[i]=j

	print(D)
	i = numpy.argmax(D)
	res=[]
	while i>=0:
		res.append(A[i])
		i=I[i]

	res = res[::-1]
	return res
# ----------------------------------------------------------------------------------------------------------------------
def LIS2(A):

	L = len(A)
	D = numpy.zeros(L,dtype=numpy.int)
	for i in range(1,L):
		if A[i]>=A[i-1]:
			D[i]=D[i-1]+1

	print(D)
	i = numpy.argmax(D)
	res = A[i-D[i]:i+1]

	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	A = numpy.array(list('12233423454345'))

	res = LIS(A)
	print(' '.join(res))

