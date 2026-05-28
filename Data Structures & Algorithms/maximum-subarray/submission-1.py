class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float('inf')
        summ = 0

        for n in nums:
            if summ < 0:
                summ = 0
            summ += n
            maxSum = max(maxSum, summ)

        return maxSum