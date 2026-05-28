class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        maxL = 0

        l = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1

            hashset.add(s[r])
            maxL = max(maxL, r - l + 1)

        return maxL