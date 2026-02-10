// Last updated: 2/9/2026, 9:54:47 PM
/**
 * // This is ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface ArrayReader {
 *     public int get(int index) {}
 * }
 */

class Solution {
    public int search(ArrayReader reader, int target) {

        int i = 0;
        
        while (reader.get(i) < Math.pow(2, 31) - 1) {
            if (reader.get(i) == target) return i;
            i++;
        }

        return -1;
    }
}