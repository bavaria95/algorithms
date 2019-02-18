class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        s = set()
        
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums) and nums[j] - nums[i] < k:
                j += 1
            if j < len(nums) and nums[j] - nums[i] == k:
                s.add((nums[i], nums[j]))
        
        return len(s)
