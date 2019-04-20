import numpy
# ----------------------------------------------------------------------------------------------------------------------
def exist_triplet_summ_S(A,S=0,elements=3):

	N = A.shape[0]
	if elements==1:
		for i in range(0, N):
			if A[i]==S:
				return True,[S]
		return False,[]

	res = False
	triplet = []
	for i in range(0,N):
		sub_array = numpy.delete(A,i)
		target = S-A[i]
		sub_res, sub_triplet = exist_triplet_summ_S(sub_array, target, elements - 1)
		if sub_res==True:
			res = True
			triplet = [A[i]]+sub_triplet

	return res, triplet
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = numpy.array(list('476123'),dtype=numpy.int)
	res, triplet = exist_triplet_summ_S(A,17)
	print(triplet)