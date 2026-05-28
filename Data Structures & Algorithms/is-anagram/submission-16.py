class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm = {}
        hm2 = {}

        for i in range(len(s)):
            hm[s[i]] = 1 + hm.get(s[i], 0)
            hm2[t[i]] = 1 + hm2.get(t[i], 0)

        return hm == hm2
