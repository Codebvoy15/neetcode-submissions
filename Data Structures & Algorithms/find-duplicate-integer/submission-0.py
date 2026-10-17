class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {} # creat a dictrionary 
        for num in nums: # iterating over keys 
            count[num] = count.get(num, 0) + 1

            if count[num] == 2:
                return num