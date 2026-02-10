// Last updated: 2/9/2026, 9:54:47 PM
class Solution {
    public String reorganizeString(String s) {
        
        //Needs a map and a heap (Map to count frequency of characters, MAX heap to order frequency)
                //reason this is MAX is because we don't want repeating chars at end of string
        Map<Character, Integer> frequency = new HashMap<>();
        char[] newS = s.toCharArray();
        for(int i = 0; i < newS.length; i++){
            frequency.put(newS[i], frequency.getOrDefault(newS[i], 0) + 1);
        }
        
        PriorityQueue<Character> byFreq = new PriorityQueue<>((a, b) -> frequency.get(b) - frequency.get(a));
        
        //add all map elements to priority queue
        byFreq.addAll(frequency.keySet());
        
        
        //while heap is greater than 1, add top two characters to stringbuilder, making sure to decrement
        //frequency on Map
        StringBuilder result = new StringBuilder();
        while(byFreq.size() > 1){
            char first =  byFreq.remove();
            char second = byFreq.remove();
            result.append(first);
            result.append(second);
            frequency.put(first, frequency.get(first) - 1);
            frequency.put(second, frequency.get(second) - 1);
            
            //if frequency of first/second is still greater than 0, add chars back to heap
            if(frequency.get(first) > 0){
                byFreq.add(first);
            }
            
            if(frequency.get(second) > 0){
                byFreq.add(second);
            }

            
        }
        
        //if the heap has a value left, make sure the frequency is not greater than 1, because if it is, return ""
        if(!byFreq.isEmpty()){
            char curr = byFreq.remove();
            if(frequency.get(curr) > 1) return "";
            else result.append(curr);
        }
        
        //convert the stringbuilder to a string and return as output
        return result.toString();
    }
}




//Good Youtube Video: https://www.youtube.com/watch?v=zaM_GLLvysw