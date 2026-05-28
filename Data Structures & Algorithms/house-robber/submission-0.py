class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 0 = 0
        # 1 = nums[1]
        # 2 = max(nums[1], nums[2])
        # 3 = max(nums[3] + nums[1], nums[2] + nums[0])
        # 4 = max(nums[4] + nums[2], nums[3] + nums[1])
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]