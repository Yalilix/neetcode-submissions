class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        prev_num = -1

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            num1 = nums[i]
            if i != 0 and nums[i - 1] == num1:
                continue

            while l < r:
                sum = num1 + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    ret.append([num1, nums[l], nums[r]])
                    l,r  = l + 1, r - 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                    
                
        return ret
            

            