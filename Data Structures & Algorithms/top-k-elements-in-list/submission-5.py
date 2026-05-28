class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i, n in enumerate(nums):
            count[n] = 1 + count.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for key, v in count.items():
            freq[v].append(key)

        ret = []
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                if k > 0:
                    ret.append(val)
                    k -= 1
                else:
                    break

        return ret                
        