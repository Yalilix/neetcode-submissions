class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashset = {}
        l = res = 0


        for r in range(len(s)):
            hashset[s[r]] = 1 + hashset.get(s[r], 0)

            if (r - l + 1) - max(hashset.values()) > k:
                hashset[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
        