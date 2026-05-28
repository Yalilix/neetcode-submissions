class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hp1 = {}
        hp2 = {}

        for i in range(len(s)):
            hp1[s[i]] = hp1.get(s[i], 0) + 1
            hp2[t[i]] = hp2.get(t[i], 0) + 1

        return hp1 == hp2