// Last updated: 2/9/2026, 9:54:04 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    public boolean isValidSequence(TreeNode root, int[] arr) {
        int[] currArr = new int[arr.length];
        int index = 0;
        return isValidSequence(root, arr, currArr, 0);
    }

    private boolean isValidSequence(TreeNode root, int[] arr, int[] currArr, int index) {
        if (root == null) return false;
        if (index > currArr.length - 1) return false;

        currArr[index] = root.val;
        index++;

        if(root.right == null && root.left == null && Arrays.equals(arr,currArr) && index == arr.length) return true;

        boolean right = isValidSequence(root.right, arr, currArr, index);
        boolean left = isValidSequence(root.left, arr, currArr, index);

        return (right || left);
    }
}