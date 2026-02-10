// Last updated: 2/9/2026, 9:54:13 PM
class Solution {
    public int connectSticks(int[] sticks) {
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a,b) -> Integer.compare(a,b));
        
        int minSum = 0;
        
        for(int iterator: sticks){
            minHeap.add(iterator);
            //System.out.println(minHeap.size());
        }
        
        while(minHeap.size() >= 2){           
            int stick1 = minHeap.remove();
            int stick2 = minHeap.remove();
            int combine = stick1 + stick2;
            minSum += combine;
            minHeap.add(combine);
        }
        
        return minSum;
        
    }
}