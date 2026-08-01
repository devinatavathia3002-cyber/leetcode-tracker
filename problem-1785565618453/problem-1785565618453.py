# Last updated: 7/31/2026, 11:26:58 PM
1class Solution:
2    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
3        l, r = 0, len(products) - 1
4        output = []
5        products = sorted(products)
6
7        for i in range(len(searchWord)):
8            prefix = searchWord[:i + 1]
9            # increment/decrement pointers
10            while l < len(products) and (len(products[l]) < len(prefix) or products[l][:i + 1] != prefix):
11                l += 1
12            while r > l and (len(products[r]) < len(prefix) or products[r][:i + 1] != prefix):
13                r -= 1
14            
15            index = l
16            ct = 0
17            res = []
18            while index <= r and ct < 3:
19                res.append(products[index])
20                index += 1
21                ct += 1
22            output.append(res)
23
24        return output
25
26