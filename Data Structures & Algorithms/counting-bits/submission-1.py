class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            cur = 0
            while i > 0:
                if i & 1 == 1:
                    cur += 1
                i >>= 1

            res.append(cur)

        return res