// Last updated: 2/9/2026, 9:54:07 PM
class Solution {
    public int sumFourDivisors(int[] nums) {
        int count = 0;
        for(int i = 0; i < nums.length; i++) {
            if(divisors(nums[i]) != null) {
                List<Integer> numbers = divisors(nums[i]);
                for(int j = 0; j < numbers.size(); j++) {
                    //System.out.println(numbers.get(j));
                    count += numbers.get(j);
                }
            }
        }
        return count;
    }

    private List<Integer> divisors(int val) {
        List<Integer> list = new ArrayList<>();
        double stopper = Math.sqrt(val);
        int amount = 2;

        if(val <= 5) return null;

        list.add(1);
        list.add(val);
        for(int k = 2; k <= stopper; k++) {

            if(val%k == 0) {
                list.add(k);
                amount++;
                if(val/k != k) {
                    list.add(val/k);
                    amount++;
                }
            }
        }
        if(amount == 4) return list;
        else return null;
    }


}