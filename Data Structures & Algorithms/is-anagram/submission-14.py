class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hp1 = {}
        hp2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hp1[s[i]] = 1 + hp1.get(s[i], 0)
            hp2[t[i]] = 1 + hp2.get(t[i], 0)

        if hp1 != hp2:
            return False

        return True
