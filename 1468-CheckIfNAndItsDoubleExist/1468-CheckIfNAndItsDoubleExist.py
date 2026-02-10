# Last updated: 2/9/2026, 9:54:01 PM
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        my_set = set()
        
        for num in arr:
            if num % 2 == 0:
                if num not in my_set and ((num * 2) in my_set or (num / 2) in my_set):
                    return True
                if num == 0 and num in my_set:
                    return True
            if num not in my_set and ((num * 2) in my_set):
                    return True
            my_set.add(num)
        
        return False