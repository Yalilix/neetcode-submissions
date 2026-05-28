class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            j = i
            val = 0
            while j:
                if j & 1:
                    val += 1
                j >>= 1
            res.append(val)
        
        return res