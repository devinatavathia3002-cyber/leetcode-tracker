# Last updated: 5/31/2026, 2:57:16 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        
4        digits.reverse()
5        res = []
6
7        carry = 1
8
9        for digit in digits:
10            carry += digit
11            if carry >= 10:
12                carry = 1
13                res.append(0)
14            else:
15                res.append(carry)
16                carry = 0
17                
18        if carry == 1:
19            res.append(carry)
20        res.reverse()
21        return res