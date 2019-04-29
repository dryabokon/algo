# leetcode.com/problems/rotate-image/
# ----------------------------------------------------------------------------------------------------------------------
import numpy
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
def rotate(A):
	# (0,1) -> (1,3)
	# (r,c) -> (c,C-1-r)
	def rotate_tuple(point, C):
		return (point[1], C - 1 - point[0])

	R = len(A)

	for r in range(0,R-1):
		for c in range(r, R-r-1):
			p1 =(r,c)
			p2 = rotate_tuple(p1, R)
			p3 = rotate_tuple(p2, R)
			p4 = rotate_tuple(p3, R)
			A[p1[0]][p1[1]] , A[p2[0]][p2[1]],A[p3[0]][p3[1]],A[p4[0]][p4[1]]=A[p4[0]][p4[1]] , A[p1[0]][p1[1]],A[p2[0]][p2[1]],A[p3[0]][p3[1]]

			'''
			p_start = (r,c)
			value = A[p_start[0]][p_start[1]]
			p_nxt = rotate_tuple(p_start,R)
			while p_start!=p_nxt:
				A[p_nxt[0]][p_nxt[1]],value =value,A[p_nxt[0]][p_nxt[1]]
				p_nxt = rotate_tuple(p_nxt,R)
			A[p_start[0]][p_start[1]] = value
			'''

	return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	#A = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]
	A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	print(numpy.array(A))
	rotate(A)
	print('------------')
	print(numpy.array(A))

	