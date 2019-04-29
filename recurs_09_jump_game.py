import numpy
# ----------------------------------------------------------------------------------------------------------------------
# leetcode.com/problems/jump-game/
def jump_game(A):

	if len(A)==1 and A[0]==0:
		return True

	res = False
	for step in range(1,A[0]+1):
		if step<len(A):
			new_game=A[step:]
			res = res or jump_game(new_game)
		elif step==len(A):
			return True

	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = [0]

	res = jump_game(A)
	print(res)