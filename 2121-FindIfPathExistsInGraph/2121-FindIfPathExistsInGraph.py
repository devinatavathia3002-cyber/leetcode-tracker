# Last updated: 2/9/2026, 9:53:52 PM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # let's do this with BFS YAY!
        
        if source == destination:
            return True
        
        # first, set up graph
        
        mapping = defaultdict(list)
        
        for i in range(len(edges)):
            mapping[edges[i][0]].append(edges[i][1])
            mapping[edges[i][1]].append(edges[i][0])
        
        queue = deque([source])
        visited = set([source])
        
        while queue:
            node = queue.popleft()
                                
            # iterate through neighbors
            for new_node in mapping[node]:
                if new_node == destination:
                    return True
                    
                if new_node not in visited:
                    queue.append(new_node)
                    visited.add(new_node)
        
        return False
                       
        