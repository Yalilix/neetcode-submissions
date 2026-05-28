class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        hashset = {}

        for i, n in enumerate(nums):
            if n in hashset:
                return True
            
            hashset[n] = i

        return False