class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hm = {}

        for (let i = 0; i < nums.length; i++) {
            const diff = target - nums[i]

            if (hm[diff] !== undefined) return [hm[diff], i]
            hm[nums[i]] = i 
        }
    }
}
