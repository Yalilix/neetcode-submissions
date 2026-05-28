class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        hm = {}

        for i, n in enumerate(nums):
            hm[n] = 1 + hm.get(n, 0)

        for key, v in hm.items():
            freq[v].append(key)

        ret = []
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                ret.append(v)
                k -= 1

                if k == 0:
                    return ret
