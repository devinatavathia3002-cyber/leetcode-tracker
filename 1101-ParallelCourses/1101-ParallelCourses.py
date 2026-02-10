# Last updated: 2/9/2026, 9:54:15 PM
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
                
        in_degree = defaultdict(int)
        for num in range(1, n + 1):
            in_degree[num] = 0
            
        out_degree = defaultdict(list)
        
        semesters = 0
        num_courses = n
        
        queue = deque()
        
        for inc, out in relations:
            out_degree[inc].append(out)
            in_degree[out] += 1
        
        for key, val in in_degree.items():
            if val == 0:
                queue.append(key)
        
        while queue:
            semesters += 1
            length = len(queue)
            num_courses -= length
            
            for i in range(length):
                course = queue.popleft()
                for node in out_degree[course]:
                    in_degree[node] -= 1
                    if in_degree[node] == 0:
                        queue.append(node)
        
        
        return semesters if num_courses == 0  else -1