class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(i, stack):
            if i == len(nums):
                ret.append(stack.copy())
                return

            stack.append(nums[i])
            backtrack(i + 1, stack)

            stack.pop()
            backtrack(i + 1, stack)
            
            return
        backtrack(0, [])

        return ret