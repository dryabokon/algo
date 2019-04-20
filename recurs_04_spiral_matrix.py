import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Print a given matrix in spiral form
# ----------------------------------------------------------------------------------------------------------------------
def print_spiral(A):
	M = A.copy()

	if M.shape[0]>0:
		if M.shape[1]!=1:
			print(M[0,:])
			M=M[1:,:]
		else:
			print(M)
			return

	if M.shape[1] > 0:
		if M.shape[0] != 1:
			print(M[:,-1])
			M=M[:,:-1]
		else:
			print(M)
			return

	if M.shape[0] > 1:
		if M.shape[1] != 1:
			print(numpy.flip(M[-1,:]))
			M=M[:-1,:]
		else:
			print(M)
			return


	if M.shape[1] > 0:
		if M.shape[0] != 1:
			print(numpy.flip(M[:,0]))
			M=M[:,1:]
		else:
			print(M)
			return

	if M.shape[0]==0 and M.shape[1]==0:
		return

	print_spiral(M)

	return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = (10*numpy.random.random_sample((5,6))).astype(int)
	print(A)
	print()
	print_spiral(A)
