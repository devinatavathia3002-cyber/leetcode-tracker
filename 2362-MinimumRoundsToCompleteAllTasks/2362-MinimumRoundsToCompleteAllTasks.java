// Last updated: 2/9/2026, 9:53:49 PM
class Solution {
    public int minimumRounds(int[] tasks) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i : tasks)
            map.put(i,map.getOrDefault(i,0)+1);
        int count = 0;
        for(int i : map.values())
        {
            if(i < 2)
                return -1;
            if(i % 3 != 0){
                count += i/3 + 1;
            }
            else count += i/3;
        }
        return count;
    }
}