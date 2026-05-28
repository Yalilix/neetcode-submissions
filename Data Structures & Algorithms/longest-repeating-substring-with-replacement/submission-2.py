class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}

        l = r = 0
        maxrepeat = 0

        while r < len(s):
            hm[s[r]] = 1 + hm.get(s[r], 0)

            curmax = max(hm.values())

            while (r - l + 1) - curmax > k:
                hm[s[l]] = hm.get(s[l], 0) - 1
                curmax = max(hm.values())
                l += 1
            print(r - l + 1, curmax)
            maxrepeat = max(maxrepeat, max(r - l + 1, curmax))
            r += 1

        return maxrepeat