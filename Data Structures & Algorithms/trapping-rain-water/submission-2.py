
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) - 1
        l = 0
        r = n
        water = 0

        lmax = 0
        rmax = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    water += lmax - height[l]
                l += 1

            else:
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    water += rmax - height[r]
                r -= 1

        return water