class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hash = {};

        for (let i = 0; i < nums.length; i++) {
            const diff = target - nums[i];
            if (hash[diff] !== undefined) {
                return [hash[diff], i]
            } 
            hash[nums[i]] = i;
        }
    }
}
