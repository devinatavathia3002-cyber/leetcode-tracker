// Last updated: 2/9/2026, 9:54:31 PM
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        
        //using binary search
        int left = 0;
        int right = arr.length - 1;
        
        //set while loop condition
        while(left < right){
            
            //set midpoint
            int midpoint = left + (right - left)/2;
            
            //if midpoint is not at decreasing value, reset left pointer
            //because we know whole left side of array is irrelevant (all increasing)
            if(arr[midpoint] < arr[midpoint + 1]){
                left = midpoint + 1;
            }
            
            //else the value we are looking at is on the "decreasing" side of the array and now
            //we have to go as far back in the array as possible until we see the first decreasing
            //value
            
            else{
                right = midpoint;
            }
        }
        
        return left;
    }
}