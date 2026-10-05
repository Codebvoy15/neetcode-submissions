class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        // loop the array 
        for( int i=0; i< nums.length; i++)
        {
           for(int j = i+1; j<nums.length; j++)
           {
            if (nums[i] + nums[j] == target)
            {
               return new int[] {i,j};
            }
           } 
            
        }
        // add the 1st element with the 2nd and so on to check if sum = target

return new int[] {};

    }
}
