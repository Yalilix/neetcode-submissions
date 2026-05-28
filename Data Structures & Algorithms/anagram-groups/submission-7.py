class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)

        for s in strs:
            hm = [0] * 26

            for c in s:
                hm[ord('z') - ord(c)] += 1

            ret[tuple(hm)].append(s)

        return list(ret.values())