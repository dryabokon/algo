import numpy
# ----------------------------------------------------------------------------------------------------------------------
# You have N eggs, from which floor in a K-floor building you can drop an egg
# Determine the minimum number of attempts to find the critical floor in the worst case
# ----------------------------------------------------------------------------------------------------------------------
def min_Egg_Attempts_Dynamic(N, K):

	A=numpy.zeros((N+1,K+1),numpy.int)
	A[1,:]=numpy.arange(0,K+1)
	A[:,1]=1
	A[0,:]=0
	A[:,0]=0

	for n in range(2, N+1):
		for k in range (2,K+1):
			worst_attempts_number=K
			for s in range (1,k):   #attempt to throw from this floor
				case1 = A[n-1,s-1]  #if broken
				case2 = A[n  ,k-s]
				attempts = 1+max(case1,case2)
				if attempts<worst_attempts_number:
					worst_attempts_number=attempts
			A[n,k]=worst_attempts_number


	return A[-1,-1]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	n_eggs = 5
	k_floors = 10
	res = min_Egg_Attempts_Dynamic(n_eggs,k_floors)
	print(res)