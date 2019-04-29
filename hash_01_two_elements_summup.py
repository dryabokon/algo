import numpy
# ----------------------------------------------------------------------------------------------------------------------
def twoSum(nums, target):
    """
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""

    dct = {}

    for i in range(len(nums)):
        if target - nums[i] not in dct:
            dct[target - nums[i]] = i
        else:
            if nums[i]==target//2:
                return i, dct[nums[i]]


    for i in range(len(nums)):
        if nums[i] in dct and dct[nums[i]]!=i:
            return i, dct[nums[i]]
    return []
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = numpy.array(list('33'),dtype=numpy.int)
    A = [3,2,4]
    res = twoSum(A, 6)
    print(numpy.array(A)[numpy.array(res)])