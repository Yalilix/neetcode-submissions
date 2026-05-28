class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minpile = r

        while l <= r:
            m = (l + r) // 2

            curpile = 0
            for pile in piles:
                curpile += math.ceil(float(pile) / m)
            
            if curpile <= h:
                minpile = min(minpile, m)
                r = m - 1
            else:
                l = m + 1

        
        return minpile

