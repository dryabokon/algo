# Longest Unique Subsequence
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def LUS2(A):


	N = len(A)
	start,stop = 0,0
	set = {A[start]:0}
	res = A[0]

	while (start<N and stop<N-1):
		next = A[stop+1]
		if next in set:
			start+=1
			stop = start
			set = {A[start]:0}
		else:
			stop += 1
			set[next]=0
			if stop-start+1>len(res):
				res=A[start:stop+1]


	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	A = numpy.array(list('1222364fghjhlw533423454345'))

	res = LUS2(A)
	print(''.join(res))