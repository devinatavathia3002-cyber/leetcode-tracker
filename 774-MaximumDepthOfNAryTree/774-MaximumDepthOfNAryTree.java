// Last updated: 2/9/2026, 9:54:49 PM
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        
        //using BFS (traversing by levels)
        
        //create variable to hold maxDepth
        int maxDepth = 0;
        //instantiate Queue to hold levels
        Queue<Node> q = new LinkedList<>();
        if(root == null) return 0;
        q.add(root);
        while(!q.isEmpty()){
            
            //make sure queue size is fixed for each level
            int size = q.size();
            for(int i = 0;i < size; i++){
                Node curr = q.remove();
                for(Node child: curr.children){
                    q.add(child);
                }
            }
            
            maxDepth++;
        }
        
        return maxDepth;
    }
}