class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                cur = n + nums[l] + nums[r]

                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    ret.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return ret