# Last updated: 2/9/2026, 9:54:06 PM
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        class Union:
            
            def __init__(self, size):
                self.parent = list(range(size))
                self.height = [1] * size
            
            def find(self, node):
                if self.parent[node] != node:
                    self.parent[node] = self.find(self.parent[node])
                return self.parent[node]
            
            def union(self, x, y):
                x_par = self.find(x)
                y_par = self.find(y)
                
                if x_par != y_par:
                    if self.height[x_par] < self.height[y_par]:
                        self.parent[x_par] = y_par
                    elif self.height[y_par] < self.height[x_par]:
                        self.parent[y_par] = x_par
                    else:
                        self.parent[y_par] = x_par
                        self.height[x_par] += 1
        
        # first, form the groups
        arr = defaultdict(list)

        u = Union(len(s))
        for i in range(len(pairs)):
            u.union(pairs[i][0], pairs[i][1])
        
        for i in range(len(s)):
            root = u.find(i)
            arr[root].append(i)
        
        s = list(s)
        for key in arr:
            vals = arr[key]
            vals.sort()
            
            print(vals)
            
            sortedChars = []
            for i in range(len(vals)):
                sortedChars.append(s[vals[i]])
                
            sortedChars.sort()
            
            for i in range(len(vals)):
                s[vals[i]] = sortedChars[i]
                
        return "".join(s)
        
                
            
            
        