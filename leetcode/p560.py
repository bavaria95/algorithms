class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        sum_by_k = [0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            sum_by_k.append(curr_sum)

        s = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if sum_by_k[j] - sum_by_k[i] == k:
                    s += 1
        
        return s
