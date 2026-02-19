# Last updated: 2/18/2026, 11:36:29 PM
1class Solution:
2    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
3        
4        q = deque()
5        q.append(startGene)
6
7        visited = set()
8        steps = 0
9
10        letters = ["A", "C", "G", "T"]
11
12        while q:
13            steps += 1
14            for i in range(len(q)):
15                gene = q.popleft()
16                if gene == endGene:
17                    return steps
18                
19                for j in range(8):
20                    # A, C, G, T
21                    for i in range(len(letters)):
22                        newGene = gene[:j] + letters[i]+ gene[j + 1:]
23                        if newGene in bank and newGene == endGene:
24                            return steps
25                        if newGene in bank and newGene not in visited:
26                            q.append(newGene)
27                            visited.add(newGene)
28        return -1