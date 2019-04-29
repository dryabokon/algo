import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Longest Unique Subsequence
def LUS(s):
	N = len(s)

	longest,i,j = 0,0,0
	set={}
	result = None

	while (i<N and j<N):
		if s[j] not in set:
			set[s[j]]=0
			j+=1
			if j-i>longest:
				longest = j - i
				result = s[i:j]
		else:
			del set[s[i]]
			i+=1

	return len(result)
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	A = numpy.array(list('12223464fghjhlw533423454345'))

	res = LUS(A)
	print(''.join(res))