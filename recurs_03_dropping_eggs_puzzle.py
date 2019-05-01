import numpy
# You have N eggs, from which floor in a K-floor building you can drop an egg
# Determine the minimum number of attempts to find the critical floor in the worst case
# ----------------------------------------------------------------------------------------------------------------------
def min_Egg_Attempts_Recursion(N, K):

	if N==0:
		return 0

	if N==1:
		return K

	if K==0:
		return 0

	if K==1:
		if N > 0:
			return 1
		else:
			return 0

	worst_attempts_number=K
	for k in range(1,K+1):
		attempts_case1 = min_Egg_Attempts_Recursion(N-1, k - 1)    #case: egg was broken
		attempts_case2 = min_Egg_Attempts_Recursion(N  , K - k)    #case: egg survived

		if 1+max(attempts_case1,attempts_case2)<worst_attempts_number:
			worst_attempts_number = 1+max(attempts_case1,attempts_case2)
	return worst_attempts_number

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	n_eggs = 5
	k_floors = 10
	res = min_Egg_Attempts_Recursion(n_eggs,k_floors)
	print(res)

	N, K = 5, 10
	R = numpy.zeros((N + 1, K + 1), dtype=numpy.int)
	for n_eggs in range(1, N + 1):
		for k_floors in range(1, K + 1):
			R[n_eggs, k_floors] = min_Egg_Attempts_Recursion(n_eggs, k_floors)

	print(R)