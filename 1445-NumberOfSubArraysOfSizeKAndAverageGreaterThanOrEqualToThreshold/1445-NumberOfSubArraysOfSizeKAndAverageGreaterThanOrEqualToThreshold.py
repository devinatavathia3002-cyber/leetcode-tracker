# Last updated: 2/9/2026, 9:54:02 PM
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        r = 0
        l = 0

        count = 0
        currSum = 0

        while r < len(arr):
            currSum += arr[r]
            if (r - l + 1) == k:
                if currSum/k  >= threshold:
                    count += 1
                currSum -= arr[l]
                l += 1
            r += 1
        return count

        