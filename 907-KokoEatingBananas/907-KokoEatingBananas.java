// Last updated: 2/9/2026, 9:54:28 PM
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        //first step is to find max value in pile
        int max = piles[0];
        for(int i = 0; i < piles.length; i++) {
            max = Math.max(max, piles[i]);
        }

        int left = 1;
        int right = max;

        while(left < right) {
            int mid = left + (right - left)/2;

            int count = 0;
            for(int i = 0; i < piles.length; i++) {
                count += Math.ceil((double)(piles[i])/mid);
            }

            if(count > h) left = mid + 1;
            else right = mid;
            //else return mid;
        }

        return right;
    }
}