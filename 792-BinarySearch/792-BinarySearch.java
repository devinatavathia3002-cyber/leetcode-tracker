// Last updated: 2/9/2026, 9:54:43 PM
class Solution {
    int retVal = -1;
    public int search(int[] nums, int target) {
        binarySearch(nums, target);
        return retVal;
    }

    public void binarySearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while(left <= right) {
            int mid = left + (right - left)/2;
            if(target < nums[mid]) {
                right = mid - 1;
            }
            else if (target > nums[mid]) {
                left = mid + 1;
            }
            else {
                retVal = mid;
                break;
            }
        }
    }
}