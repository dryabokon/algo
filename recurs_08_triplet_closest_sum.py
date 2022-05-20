# ----------------------------------------------------------------------------------------------------------------------
def triplet_closest_S(A, S=0):

	A.sort()
	best_sum = A[0] + A[1] + A[2]
	for i in range(len(A) - 2):
		j, k = i + 1, len(A) - 1
		while j < k:
			sum = A[i] + A[j] + A[k]
			if sum == S:
				return sum

			if abs(sum - S) < abs(best_sum - S):
				best_sum = sum

			if sum < S:
				j += 1
			elif sum > S:
				k -= 1

	return best_sum

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	A = [-1,2,1,-4]
	res = triplet_closest_S(A,1)
	print(res)