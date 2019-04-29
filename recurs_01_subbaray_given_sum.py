import numpy
# ----------------------------------------------------------------------------------------------------------------------
def subarray_given_sum(A,S):

	result = []
	for each in A:
		if int(each)==S:
			result.append([int(S)])

	if A.shape[0]<=1:
		return result

	for i in range(0,A.shape[0]):
		temp_array = numpy.delete(A,i)
		temp_array = temp_array[numpy.where(temp_array<=A[i])]

		temp_result = subarray_given_sum(temp_array,S-A[i])
		for each in temp_result:
			if len(each)>0:
				result.append([int(A[i])]+each)

	return result
# ----------------------------------------------------------------------------------------------------------------------
def subarray_given_sum_can_reuse(A, target):

	result = []
	for each in A:
		if int(each)==target:
			result.append([int(target)])

	for i in range(0,A.shape[0]):
		temp_list = A[numpy.where(A<=A[i])]

		if target - A[i]>=0:
			temp_res = subarray_given_sum_can_reuse(temp_list,target - int(A[i]))
			for each in temp_res:
				result.append([int(A[i])]+each)


	return result
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list('236347123')
	A = list(set(A))
	A.sort()
	A = numpy.array(A,dtype=numpy.int)


	res = subarray_given_sum_can_reuse(A,12)
	for each in res:
		print(each)