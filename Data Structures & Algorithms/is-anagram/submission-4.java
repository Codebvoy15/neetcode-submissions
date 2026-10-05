class Solution {
    public boolean isAnagram(String s, String t) {

        // first check the length of strings
        
        int lenS = s.length();
        int lenT = t.length(); 
        // if equal , 
        
        if(lenS == lenT)
        {
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
         
        Arrays.sort(sArray);
        Arrays.sort(tArray);

         return Arrays.equals(sArray, tArray);
         }

         return false;
        // sort the string1
        // sort the string 2

        // check if both strings are equal

        // if yes -> true

        //else -> false 
        
        
        //else retrun false 

        //
    }
}
