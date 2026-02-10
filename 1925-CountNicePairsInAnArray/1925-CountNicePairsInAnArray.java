// Last updated: 2/9/2026, 9:53:55 PM
class Solution {
    public int countNicePairs(int[] nums) {
        Map<Integer, Integer> reverse = new HashMap<>();
        long count = 0;

        for (int i = 0; i < nums.length; i++) {
            int reversed = reverse(nums[i]);
            int finalized = nums[i] - reversed;
            if (reverse.containsKey(finalized)) count += reverse.get(finalized);
            reverse.put(finalized, reverse.getOrDefault(finalized, 0) + 1);
        }

        return (int)(count%(Math.pow(10,9) + 7));
    }

    private int reverse(int num) {
        int res = 0;
        while (num != 0) {
            int addition = num%10;
            res = res * 10 + addition;
            num = num/10;
        }
        return res;
    }
}