# Last updated: 2/9/2026, 9:54:51 PM
from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        queue = deque()
        visited = set(deadends)  
        
        totalTurns = float('inf')
        
        if '0000' in visited:
            return -1 
        
        queue.append(('0000', 0))
        visited.add('0000')  
        
        def addLeaves(lock_tuple):
            lock, steps = lock_tuple  # Fix 3: Ensure `lock` and `steps` are properly extracted
            
            for i in range(4):
                # Add 1 and add to queue
                addedLock = str((int(lock[i]) + 1) % 10)
                addedLock = lock[:i] + addedLock + lock[i + 1:]
                
                if addedLock not in visited:
                    queue.append((addedLock, steps + 1))  # Fix 4: Use correct `steps`
                    visited.add(addedLock)
                
                # Subtract 1 and add to queue
                subtrackLock = str((int(lock[i]) + 10 - 1) % 10)
                subtrackLock = lock[:i] + subtrackLock + lock[i + 1:]
                
                if subtrackLock not in visited:
                    queue.append((subtrackLock, steps + 1))  # Fix 4: Use correct `steps`
                    visited.add(subtrackLock)
        
        while queue:
            currNum, steps = queue.popleft()
                  
            if currNum == target:
                return steps  
            
            addLeaves((currNum, steps))  
        
        return -1  
