class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for key, val in hm.items():
            freq[val].append(key)

        ret = []
        for i in range(len(nums), 0, -1):
            for val in freq[i]:
                if k > 0:
                    ret.append(val)
                    k -= 1
        
        return ret