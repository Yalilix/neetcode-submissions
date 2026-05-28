class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1
        while (l < r):
            while (l < r and (numbers[r] + numbers[l] < target)):
                l += 1;
            while (r > l and (numbers[r] + numbers[l] > target)):
                r -= 1;
        

            if (numbers[r] + numbers[l] == target):
                return [l + 1, r + 1];