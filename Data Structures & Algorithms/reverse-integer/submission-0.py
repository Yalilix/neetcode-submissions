class Solution:
    def reverse(self, x: int) -> int:
        def rec(n: int, res: int) -> int:
            if n == 0:
                return res

            res = res * 10 + n % 10
            return rec(n // 10, res)

        sign = -1 if x < 0 else 1
        x = abs(x)
        revNum = rec(x, 0)
        revNum *= sign

        if revNum < -(1 << 31) or revNum > (1 << 31) - 1:
            return 0
        
        return revNum