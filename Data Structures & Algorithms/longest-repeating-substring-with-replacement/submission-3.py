class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        maxrepeat = 0

        l = r = 0
        maxf = 0
        while r < len(s):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            maxf = max(maxf, hm[s[r]])
            
            while (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1

            maxrepeat = max(maxrepeat, r - l + 1)
            r += 1

        return maxrepeat