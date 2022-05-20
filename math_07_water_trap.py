# https://leetcode.com/problems/trapping-rain-water/
# ----------------------------------------------------------------------------------------------------------------------
def max_area2(H):
	left, right = 0, len(H) - 1
	areas = 0
	while left != right:
		if H[left] < H[right]:
			areas = max((right - left) * H[left], areas)
			left += 1
		else:
			areas = max((right - left) * H[right], areas)
			right -= 1
	return areas
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


	H = [1, 8, 6, 2, 5, 4, 8, 3, 7]
	#res = 49
	res = max_area2(H)
	print(res)

