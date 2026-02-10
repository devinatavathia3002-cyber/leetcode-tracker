// Last updated: 2/9/2026, 9:54:03 PM
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
    int totalCount = 0;
    public int goodNodes(TreeNode root) {
        if(root == null) return 0;
        findCount(root, root.val);
        return totalCount;
    }

    private void findCount(TreeNode root, int max) {
        if(root == null) return;
        if(root.val >= max) {
            totalCount++;
            findCount(root.right, root.val);
            findCount(root.left, root.val);
        }
        else {
            findCount(root.right, max);
            findCount(root.left, max);
        }
    }
}