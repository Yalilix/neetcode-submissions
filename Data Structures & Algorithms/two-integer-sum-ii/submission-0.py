class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}

        for i, num in enumerate(numbers):
            if target - num in hashset:
                return [hashset[target - num], i + 1]
            hashset[num] = i + 1