class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not self.isAlphaNum(s[l].lower()) and l < r:
                l += 1
            elif not self.isAlphaNum(s[r].lower()) and r > l:
                r -= 1
            elif s[l].lower() == s[r].lower():
                l, r = l + 1, r - 1
            else:
                return False
        
        return True
        

    def isAlphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))