class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        n = len(nums)
        def dfs(i, arr, total):
            if total == target:
                ret.append(arr.copy())
                return
            
            if sum(arr) > target or i >= n:
                return

            arr.append(nums[i])
            dfs(i, arr, total + nums[i])
            arr.pop()
            dfs(i + 1, arr, total)

        dfs(0, [], 0)

        return ret