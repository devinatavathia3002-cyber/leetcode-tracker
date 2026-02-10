# Last updated: 2/9/2026, 9:54:16 PM
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        class UnionFind:
            
            def __init__(self, size):
                self.parent = list(range(size))
                self.height = [1] * size
            
            def find(self, node):
                if self.parent[node] != node:
                    self.parent[node] = self.find(self.parent[node])
                return self.parent[node]
            
            def union(self, x, y):
                x_parent = self.find(x)
                y_parent = self.find(y)
                
                if x_parent != y_parent:
                    if self.height[x_parent] < self.height[y_parent]:
                        self.parent[x_parent] = y_parent
                    
                    elif self.height[y_parent] < self.height[x_parent]:
                        self.parent[y_parent] = x_parent
                    
                    else:
                        self.parent[x_parent] = y_parent
                        self.height[y_parent] += 1
            
        u = UnionFind(n)
        node_number = n
        
        logs.sort()
        
        for i in range(len(logs)):

            x_node = logs[i][1]
            y_node = logs[i][2]
            
            x_parent = u.find(x_node)
            y_parent = u.find(y_node)
            
            if x_parent != y_parent:
                u.union(x_node, y_node)
                node_number -= 1
                
                if node_number == 1:
                    return logs[i][0]
        
        return -1
            
                            