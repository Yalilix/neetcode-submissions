class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        
        for i, n in enumerate(nums):
            if n in hm:
                return True
            
            hm[n] = i

        return False
