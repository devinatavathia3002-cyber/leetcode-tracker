// Last updated: 2/9/2026, 9:54:26 PM
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] returnArray = new int[nums.length];
        int returnPointer = 0;
        int right = 0;
        int left = 0;

        while (nums[right] < 0 && right < nums.length - 1) {
            right++;
        }
        if (nums.length != 1) {
            left = right - 1;
        }

        while (left >= 0 && right < nums.length) {
            if (Math.abs(nums[right]) < Math.abs(nums[left])) {
                returnArray[returnPointer] = Math.abs(nums[right]) * Math.abs(nums[right]);
                right++;
                returnPointer++;
                if (right >= nums.length) break;
            }
            else {
                returnArray[returnPointer] = Math.abs(nums[left]) * Math.abs(nums[left]);
                left--;
                returnPointer++;
                if (left < 0) break;
            }
        }

        while (right < nums.length && returnPointer < nums.length) {
            returnArray[returnPointer] = Math.abs(nums[right]) * Math.abs(nums[right]);
            right++;
            returnPointer++;
        }

        while (left >= 0 && returnPointer < nums.length) {
            returnArray[returnPointer] = Math.abs(nums[left]) * Math.abs(nums[left]);
            left--;
            returnPointer++;
        }


        return returnArray;
    }
}