// Last updated: 2/9/2026, 9:54:27 PM
class Solution {
    public int totalFruit(int[] fruits) {
        int basket1 = fruits[0];
        int basket2 = fruits[0];

        int left = 0;
        int right = 1;

        int longest = 0;

        while (right < fruits.length) {
            int curr = fruits[right];
            if (curr != basket1 && curr != basket2) {
                if (basket1 == basket2) basket2 = curr;
                else {
                    int length = right - left;
                    longest = Math.max(longest, length);

                    basket1 = curr;
                    basket2 = fruits[right - 1];

                    left = right - 1;

                    while (left >= 0) {
                        if (fruits[left] == basket1 || fruits[left] == basket2) left--;
                        else break;
                    }

                    left++;
                    System.out.println(left);
                }
            }
            right++;
        }

        

        longest = Math.max(longest, right - left);

        return longest;
    }
}