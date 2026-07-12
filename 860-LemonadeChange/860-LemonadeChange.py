# Last updated: 7/11/2026, 6:09:12 PM
1class Solution:
2    def lemonadeChange(self, bills: List[int]) -> bool:
3        if bills[0] != 5:
4            return False
5        
6        fives = 1
7        tens = 0
8
9        for i in range(1, len(bills)):
10            amt = bills[i]
11            if amt == 5:
12                fives += 1
13            elif amt == 10:
14                if fives == 0:
15                    return False
16                tens += 1
17                fives -= 1
18            else:
19                # amt is 20
20                if fives == 0:
21                    return False
22
23                if tens >= 1:
24                    tens -= 1
25                    fives -= 1
26                else:
27                    if fives >= 3:
28                        fives -= 3
29                    else:
30                        return False
31
32        return True