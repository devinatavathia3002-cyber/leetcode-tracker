// Last updated: 2/9/2026, 9:54:20 PM
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        
        //Integer.Compare() will only give you minHeap, here we want to use maxHeap
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b) -> dist(b) - dist(a));
        
        int[][] res = new int[k][2];
        
        //make for loop to go through each array points accordingly.
        //add coordinates to maxHeap, making sure heap only stores k num
        //values at a time
        for(int[] iterator: points){
            
            maxHeap.add(iterator);
            while(maxHeap.size() > k){
                maxHeap.remove();
            }
            
        }
        
        //add maxHeap contents to result array
        int i = 0;
        while(!maxHeap.isEmpty()){
            //System.out.println(maxHeap.size());
            res[i] = maxHeap.remove();
            i++;
        }
        return res;
    }
    
    public int dist(int[] points){
        int x = points[0];
        int y = points[1];
        return x*x + y*y;
    }
}


//Good Video: https://www.youtube.com/watch?v=dMtnQnhbijk