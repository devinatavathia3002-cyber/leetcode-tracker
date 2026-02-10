// Last updated: 2/9/2026, 9:53:55 PM
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {
        
        
        //basic overview of this problem is that we need to constantly check to make sure
        //both nodes q and p are either in the left or right side of the binary tree. If they 
        //are not this means that they no longer have a deeper LCA and the recrusion hits base case.
        
        //this is a twist on the classic binary tree problem where instaed of having a root node passed in
        //and exploring each level, we are only given a way to access p.parent or q.parent. The way to 
        //approach this is to create a hashset with the all nodes on the path to p and then recurse upwards
        //from the q node until we get to a point where the parent is not contained within the hashet (path
        //to the p node)
        
        HashSet<Node> pathToP = new HashSet<>();
        while(p != null){
            pathToP.add(p);
            p = p.parent;
        }
        
        while(!pathToP.contains(q)){
            q = q.parent;
        }
        
        return q;
    }
}