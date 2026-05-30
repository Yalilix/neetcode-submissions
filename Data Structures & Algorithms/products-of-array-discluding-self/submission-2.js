class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const ret1 = [1]

        for (let i = 1; i < nums.length; i++) {
            ret1.push(nums[i - 1] * ret1[i - 1])
        }

        console.log(ret1)

        const ret2 = new Array(nums.length).fill(1)
        for (let i = nums.length - 2; i >= 0; i--) {
            ret2[i] = nums[i + 1] * ret2[i + 1]
        }
        console.log(ret2)

        for (let i = 0; i < nums.length; i++) {
            ret1[i] = ret1[i] * ret2[i]
        }
        
        return ret1
    }
}
