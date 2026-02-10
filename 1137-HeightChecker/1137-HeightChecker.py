# Last updated: 2/9/2026, 9:54:11 PM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        heightsSorted = sorted(heights)
        
        num = 0
        
        for i in range(len(heights)):
            if heights[i] != heightsSorted[i]:
                num += 1
        
        return num