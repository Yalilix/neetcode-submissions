class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxwater = 0

        while l < r:
            minlen = min(heights[l], heights[r])

            cur = minlen * (r - l)

            if cur > maxwater:
                maxwater = cur   
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxwater
            

