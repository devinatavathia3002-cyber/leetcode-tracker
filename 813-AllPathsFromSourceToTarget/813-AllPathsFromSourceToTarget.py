# Last updated: 2/9/2026, 9:54:39 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        n = len(graph)
        
        queue = deque([[0]])
        # visited = set([0])
        
        while queue:
            currPath = queue.popleft()
            currNode = currPath[-1]
            
            for neighbor in graph[currNode]:
                newPath = currPath + [neighbor]
                
                if neighbor == (n - 1):
                    res.append(newPath)
                
                else:
                    queue.append(newPath)
        
        return res