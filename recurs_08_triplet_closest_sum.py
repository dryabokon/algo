import numpy
# ----------------------------------------------------------------------------------------------------------------------
def triplet_closest_S(A, S=0, elements=3):

	N = len(A)
	if elements==1:
		res =[]
		for i in range(0, N):
			res.append([A[i]])
		return res

	triplets = []
	for i in range(0,N):
		sub_array = A[i+1:]
		sub_triplets = triplet_closest_S(sub_array, 0, elements - 1)
		for each in sub_triplets:
			triplets.append([A[i]]+each)


	if elements==3:
		best, value = 0, abs((sum(triplets[0]) - S))
		for i in range(1,len(triplets)):
			if abs((sum(triplets[i])-S))<value:
				best=i
				value = abs((sum(triplets[i])-S))
		return triplets[best]
	else:
		return triplets
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = numpy.array(list('476123'),dtype=numpy.int)

	res = triplet_closest_S(A, 18)
	print(res)