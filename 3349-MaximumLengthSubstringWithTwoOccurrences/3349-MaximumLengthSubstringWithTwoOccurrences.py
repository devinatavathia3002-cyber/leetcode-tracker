# Last updated: 2/9/2026, 9:53:48 PM
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0

        maxLen = 0

        mydict = {}

        while right < len(s):
            if s[right] not in mydict:
                mydict[s[right]] = 1
                maxLen = max(maxLen, right - left + 1)
                right += 1
            else:
                while mydict[s[right]] > 1:
                    mydict[s[left]] = mydict[s[left]] - 1
                    left += 1
                mydict[s[right]] = mydict[s[right]] + 1
                maxLen = max(maxLen, right - left + 1)
                right += 1
        return maxLen



        