class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const ret = []
        nums.sort((a, b) => a - b)

        for (let i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] === nums[i - 1]) continue
            const num1 = nums[i]

            let j = i + 1
            let k = nums.length - 1
            while (j < k) {
                const cur = num1 + nums[j] + nums[k]
                if (cur > 0) {
                    k--
                } else if (cur < 0) {
                    j++
                } else {
                    ret.push([num1, nums[j], nums[k]])
                    j++

                    while (j < k && j < nums.length && nums[j - 1] === nums[j]) {
                        j++
                    }
                }
            }
        }
        return ret
    }
}
