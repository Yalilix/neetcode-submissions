class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_substr = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]
                l, r = 0, len(substr) - 1

                while l <= r:
                    if substr[l] != substr[r]:
                        break

                    l, r = l + 1, r - 1
                
                if l > r and len(substr) > len(long_substr):
                    long_substr = substr

        return long_substr

                    