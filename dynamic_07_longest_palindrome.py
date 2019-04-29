import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Longest Palindromic Subsequence
def LPS(s):
	'''
	:type s: str
    :rtype: str
	'''
	N = len(s)
	A = numpy.eye(N,dtype=numpy.int)
	max_value=1
	start,stop=0,0
	for i in range(1,N-1):
		for step in range(1,min(i,N-1-i)+1):
			A[i-step,i+step]=A[i-step+1,i+step-1] and s[i-step]==s[i+step]
			if A[i-step,i+step]>0:
				if 1+2*step>max_value:
					max_value = 1+2*step
					start,stop = i-step,i+step

	for i in range(1, N):
		A[i-1,i] = (s[i] == s[i - 1])
		if A[i - 1 , i ] > 0:
			if 2>max_value:
				max_value = 2
				start, stop = i - 1 , i
		xxx = min(i-1,N-1-i)
		for step in range(1,xxx+1):

			A[i-1-step, i+step] = (s[i+step] == s[i-step - 1]) and A[i-1-step+1, i+step-1]
			if A[i - 1 - step, i + step]>0:
				if 2+2*step > max_value:
					max_value = 2+2*step
					start, stop = i-1 - step, i + step

	print(A)
	print(max_value)

	return s[start:stop+1]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	s = 'hhaahahahahaha'
	res = LPS(s)
	print(res)