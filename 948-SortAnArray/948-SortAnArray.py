# Last updated: 2/9/2026, 9:54:24 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums):
            
            if len(nums) <= 1:
                return nums
            
            else:
                pivotIndex = len(nums) // 2
                left = mergeSort(nums[:pivotIndex])
                right = mergeSort(nums[pivotIndex:])
                
                return merging(left, right)
        
        def merging(left, right):
            
            l, r = 0, 0
            
            finalArr = []
            
            while l < len(left) and r < len(right):
                
                if left[l] < right[r]:
                    finalArr.append(left[l])
                    l += 1
                
                else:
                    finalArr.append(right[r])
                    r += 1
            
            if l < len(left):
                finalArr.extend(left[l:])
            if r < len(right):
                finalArr.extend(right[r:])
            
            return finalArr
        
        return mergeSort(nums)