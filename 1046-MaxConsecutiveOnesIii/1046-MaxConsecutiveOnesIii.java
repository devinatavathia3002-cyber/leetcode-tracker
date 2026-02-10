// Last updated: 2/9/2026, 9:54:18 PM
class Solution {
    public int longestOnes(int[] nums, int k) {
        int right = 0;
        int left = 0;
        int maxLength = 0;
        int numLeft = k;

        while (right < nums.length) {
            if (nums[right] != 1) {
                if (numLeft > 0) {
                    numLeft--;
                }
                else {
                    if (k > 0) {
                        left = right;
                        numLeft = k - 1;
                        while (left > 0) {
                            left--;
                            if (nums[left] != 1) {
                                if (numLeft > 0) {
                                    numLeft--;
                                }
                                else {
                                    left++;
                                    break;
                                }
                            }
                        }
                    }
                    else {
                        left = (right + 1);
                    }
                }
            }
            if (right - left + 1 > maxLength) {
                maxLength = right - left + 1;
            }
            right++;
        }
        return maxLength;
    }
}