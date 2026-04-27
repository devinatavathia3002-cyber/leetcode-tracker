# Last updated: 4/26/2026, 8:32:06 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3
4        for i in range(2, len(cost)):
5            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
6        
7        return min(cost[len(cost) - 1], cost[len(cost) - 2])
8
9