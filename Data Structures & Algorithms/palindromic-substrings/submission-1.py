class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    # if i < 0 or j - 1 < 0 or i + 1 >= n or j >= n:
                    #     continue

                    if j - i <= 2:
                        cnt += 1
                    else:
                        if dp[i + 1][j - 1]:
                            cnt += 1


        return cnt