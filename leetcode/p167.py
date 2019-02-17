class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]

            if s > target:
                r -= 1
            
            if s < target:
                l += 1
        
        return False
