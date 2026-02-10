# Last updated: 2/9/2026, 9:53:53 PM
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0

        total = 0

        while r < len(s):
            if (r - l + 1) == 3:
                if len(set(s[l:r+1])) == 3:
                    total += 1
                    l += 1
                else:
                    l += 1
            r += 1

        
        return total

        