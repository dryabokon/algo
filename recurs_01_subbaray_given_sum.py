import numpy
# ----------------------------------------------------------------------------------------------------------------------
def subarray_given_sum(A,S):

	subarray = None
	for each in A:
		if each==S:
			subarray=numpy.array([S])

	for i in range(0,A.shape[0]):
		temp_S = S-A[i]
		temp_array = numpy.delete(A,i)
		result = subarray_given_sum(temp_array,temp_S)
		if result is not None:
			subarray = numpy.insert(result,0,A[i])

	return subarray
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = numpy.array(list('476123'),dtype=numpy.int)
	res = subarray_given_sum(A,10)
	print(res)