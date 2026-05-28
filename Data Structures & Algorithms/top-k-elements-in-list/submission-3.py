class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        hp = {}

        for i, n in enumerate(nums):
            hp[n] = 1 + hp.get(n, 0)

        for key, v in hp.items():
            freq[v].append(key)

        ret = []
        for i in range(len(nums), 0, -1):
            for val in freq[i]:
                if k > 0:
                    ret.append(val)
                    k -= 1

        return ret