class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        
        for i, n in enumerate(nums):
            if n in hash:
                return True
            
            hash[n] = i
            
        return False