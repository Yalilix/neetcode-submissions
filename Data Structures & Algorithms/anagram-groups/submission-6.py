class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            hp = [0] * 26
            for c in s:
                hp[ord(c) - ord('a')] += 1

            res[tuple(hp)].append(s)

        return list(res.values())
        

