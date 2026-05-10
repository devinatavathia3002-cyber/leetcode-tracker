# Last updated: 5/9/2026, 11:18:17 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        
4        if sum(gas) < sum(cost):
5            return -1
6
7        res = 0
8        total = 0
9
10        for i in range(len(gas)):
11            val = gas[i] - cost[i]
12            total += val
13            if total < 0:
14                total = 0
15                res = i + 1
16
17        return res