# Last updated: 5/10/2026, 6:52:18 PM
1class Solution:
2    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
3        
4        # with hashmap
5
6        if len(hand) % groupSize != 0:
7            return False
8
9        count = defaultdict(int)
10        for val in hand:
11            count[val] += 1
12        
13        for num in sorted(hand):
14            if count[num] == 0:
15                continue
16            start = num
17            while count[start] > 0:
18                start -= 1
19            
20            start += 1
21            for j in range(start, start + groupSize):
22                if count[j] == 0:
23                    return False
24                count[j] -= 1
25
26        return True