class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        for k in range(len(nums)):
            val = nums[k]
            nums[k] = 2
            if val < 2:
                nums[i] = 1
                i += 1
            if val == 0:
                nums[j] = 0
                j += 1
