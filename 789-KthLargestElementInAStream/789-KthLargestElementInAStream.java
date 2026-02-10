// Last updated: 2/9/2026, 9:54:44 PM
class KthLargest {
    
    private static int k;
    private PriorityQueue<Integer> minHeap;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        minHeap = new PriorityQueue<>((a,b) -> Integer.compare(a,b));
        
        for(int iterator: nums){
            minHeap.add(iterator);
        }
        
        while(minHeap.size() > k){
            minHeap.remove();
        }
        
    }
    
    public int add(int val) {
        
        minHeap.add(val);
        while(minHeap.size() > k){
            minHeap.remove();
        }
        
        return minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */