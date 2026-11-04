class Solution:
    def search(self, nums: List[int], target: int) -> int:


    #    for i in range(len(nums)):
    #         if nums[i] == target:
    #             return i

    #         return -1

    # firt find mid
    # if target > mid :
        # search right
    #else: 
        # search Left



        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            elif target > nums[mid]:
                l = mid+1

            else:
                r = mid -1

        return -1

