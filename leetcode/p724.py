class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_by_k = [0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            sum_by_k.append(curr_sum)
        
        for i in range(n):
            if sum_by_k[i] - sum_by_k[0] == sum_by_k[-1] - sum_by_k[i + 1]:
                return i
        
        return -1
