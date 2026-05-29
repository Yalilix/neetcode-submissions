class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {}

        for (const n of nums) {
            count[n] = 1 + (count[n] || 0)
        }
        
        const fq = Array.from( { length: nums.length + 1 }, () => [])
        for (const [key, val] of Object.entries(count)) {
            fq[val].push(key)
        }

        let res = []
        for (let i = nums.length; i > 0; i--) {
            for (const cur of fq[i]) {
                if (k > 0) {
                    res.push(cur)
                    k--
                }
            }
        }
        return res   
    }
}
