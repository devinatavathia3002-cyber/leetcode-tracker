// Last updated: 2/9/2026, 9:53:57 PM
class Solution {
    public int[] frequencySort(int[] nums) {
        
        int[] returnArr = new int[nums.length];
        
        HashMap<Integer, Integer> map = new HashMap<>();
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a,b) -> map.get(a) == map.get(b)?b-a: Integer.compare(map.get(a), map.get(b)));
            
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        
         for (Map.Entry<Integer,Integer> iterator : map.entrySet()){
             minHeap.add(iterator.getKey());
         }
        
                    int j = 0;
        while(!minHeap.isEmpty()){
            int currElement = minHeap.remove();
            for(int k = 0; k < map.get(currElement); k++){
                returnArr[j] = currElement;
                j++;
            }
        }
        
        return returnArr;
    }
}