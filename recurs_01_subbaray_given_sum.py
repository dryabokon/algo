import numpy

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
def subarray_given_sum(A,S):

	res = []
	for i,a in enumerate(A):
		if int(a)==S:
			res.append([a])
		elif int(a)<S:
			A_temp = numpy.delete(A,i)
			temp_res = subarray_given_sum(A_temp,S-int(a))
			for each in temp_res:
				res.append([int(a)]+each)

	return res
# ----------------------------------------------------------------------------------------------------------------------
def subarray_given_sum_unique(A,S,minvalue=None):

	res = []
	for i,a in enumerate(A):
		a = int(a)
		if minvalue is not None and a <= minvalue:continue
		if a==S:
			res.append([a])
		else:
			A_temp = numpy.delete(A,i)
			temp_res = subarray_given_sum_unique(A_temp,S-a,a)
			for each in temp_res:
				res.append([a]+each)

	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list('236347123')
	A = list(set(A))
	A.sort(reverse=True)
	A = numpy.array(A,dtype=numpy.int)


	res = subarray_given_sum_unique(A,12)
	for each in res:
		print(each)

