class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        hp = defaultdict(int)

        for i, n in enumerate(nums):
            hp[n] += 1

        for key, val in hp.items():
            freq[val].append(key)
        
        print(freq)
        ret = []
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                if k == 0:
                    break

                if k > 0:
                    ret.append(val)
                    k -= 1

        return ret
