class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hp = {}

        for i, n in enumerate(nums):
            if n in hp:
                return True

            hp[n] = i

        return False
            
