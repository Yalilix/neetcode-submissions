class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i in range(len(nums)):
            num = nums[i]
            if target - num in hashset:
                if i > hashset[target - num]:
                    return [hashset[target - num], i]
                return [i, hashset[target - num]]
            hashset[num] = i
