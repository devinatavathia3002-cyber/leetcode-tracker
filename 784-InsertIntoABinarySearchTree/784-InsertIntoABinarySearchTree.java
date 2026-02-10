// Last updated: 2/9/2026, 9:54:48 PM
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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null) return new TreeNode(val);
        TreeNode current_val = root;
        while(true){
            if(current_val.val > val){
                if(current_val.left != null){
                    current_val = current_val.left;
                }
                else{
                    current_val.left = new TreeNode(val);
                    break;
                }
            }
            if(current_val.val < val){
                if(current_val.right != null){
                    current_val = current_val.right;
                }
                else{
                    current_val.right = new TreeNode(val);
                    break;
                }
            }
        }
        return root;
    }
}