class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        s = s.lower()
        i = 0
        while i < len(s) and j >= 0:
            # print(s[i], 1)
            # print(i,j)
            if (not s[j].isalpha()):
                j -= 1
                continue
            
            if (not s[i].isalpha() and not s[i].isnumeric()):
                i += 1
                continue
            
            if (s[i] != s[j]):
                print(i, j)
                return False
            j -= 1
            i += 1
        return True