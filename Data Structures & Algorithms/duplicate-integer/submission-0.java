class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        // create an empty hash set
        // Loop through the array
        HashSet<Integer> numSet =  new HashSet<>();
         
        for(int num:nums){
            if (numSet.contains(num)){
                return true;
            }
            numSet.add(num);
        }
        return false;
        // store each of the values in the hash

        // loop through the array and compare each elemeet if its therer in the hash table

    }
}
