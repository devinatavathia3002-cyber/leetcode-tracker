# Last updated: 4/23/2026, 10:58:45 PM
1class Solution:
2    def alienOrder(self, words: List[str]) -> str:
3
4        # form adjacency list
5        adj = defaultdict(list)
6        indegree = defaultdict(int)
7        for word in words:
8            for c in word:
9                indegree[c] = 0
10
11        for i in range(len(words) - 1):
12            w1 = words[i]
13            w2 = words[i + 1]
14
15            if len(w2) < len(w1) and w1[:len(w2)] == w2:
16                return ""
17            
18            for j in range(min(len(w1), len(w2))):
19                if w1[j] != w2[j]:
20                    if w2[j] not in adj[w1[j]]:
21                        adj[w1[j]].append(w2[j])
22                        indegree[w2[j]] += 1
23                    break
24        
25        # conduct topo sort
26        q = deque()
27        for c in indegree:
28            if indegree[c] == 0:
29                q.append(c)
30        output = ""
31
32        while q:
33            curr = q.popleft()
34            output += curr
35
36            for nei in adj[curr]:
37                indegree[nei] -= 1
38                # adj[curr].remove(nei)
39                if indegree[nei] == 0:
40                    q.append(nei)
41
42
43        if len(output) != len(indegree.keys()):
44            return ""
45        return output
46            