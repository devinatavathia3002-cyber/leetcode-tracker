# Last updated: 2/9/2026, 9:54:04 PM
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for i in nums:
            internalCount = 0
            while i > 0:
                internalCount += 1
                i = (i // 10)
            if internalCount % 2 == 0:
                count += 1
        
        return count
        