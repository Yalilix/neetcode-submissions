class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hm = new Set()

        for (const n of nums) {
            if (hm.has(n)) return true

            hm.add(n)
        }

        return false
    }
}
