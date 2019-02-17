class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            d[target - num] = i

        for i, num in enumerate(nums):
            if num in d:
                ind2 = d[num]
                if i != ind2:
                    return [i, d[num]]
