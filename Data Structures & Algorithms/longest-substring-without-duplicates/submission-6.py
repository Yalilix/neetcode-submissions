class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        maxL = 0
        l, r = 0, 0

        while r < len(s):
            print(hs)
            while s[r] in hs:
                hs.remove(s[l])
                l += 1

            hs.add(s[r])
            maxL = max(maxL, r - l + 1)
            r += 1

        return maxL
