// Last updated: 2/9/2026, 9:54:17 PM
class Solution {
    public int twoSumLessThanK(int[] nums, int k) {
        
        Arrays.sort(nums);

        int left = 0;
        int right = nums.length - 1;

        int max = -1;

        while (left < right) {

            int sum = nums[left] + nums[right];
            if (sum == k || sum > k) right--;
            else {
                max = Math.max(max, sum);
                left++;
            }
        }

        return max;
    }
}