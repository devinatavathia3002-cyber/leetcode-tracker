# Last updated: 2/9/2026, 9:54:32 PM
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        queue = deque()
        
        def appendAllVals(roomNumber):
            if roomNumber not in visited:
                for num in rooms[roomNumber]:
                    queue.append(num)
                
        appendAllVals(0)
        visited.add(0)
        
        while queue:
            currVal = queue.popleft()            
            appendAllVals(currVal)
            visited.add(currVal)

        
        print(len(visited))
        return len(visited) == (len(rooms))
        
        
            
        
        