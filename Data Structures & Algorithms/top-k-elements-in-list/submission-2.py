class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        for key, val in hashmap.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
