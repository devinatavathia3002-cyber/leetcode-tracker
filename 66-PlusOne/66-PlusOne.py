# Last updated: 5/31/2026, 3:25:41 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        
4        # # iteration 1 solution
5        # digits.reverse()
6        # res = []
7
8        # carry = 1
9
10        # for digit in digits:
11        #     carry += digit
12        #     if carry >= 10:
13        #         carry = 1
14        #         res.append(0)
15        #     else:
16        #         res.append(carry)
17        #         carry = 0
18
19        # if carry == 1:
20        #     res.append(carry)
21        # res.reverse()
22        # return res
23
24        # iteraiton 2
25        for i in range(len(digits) - 1, - 1, -1):
26            if digits[i] + 1 <= 9:
27                digits[i] += 1
28                return digits
29            else:
30                digits[i] = 0
31        
32        return [1] + digits