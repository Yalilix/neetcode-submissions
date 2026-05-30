class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const list = new Set(nums)
        let ret = 0

        for (const n of list) {
            if (list.has(n - 1)) continue

            let curlen = 0
            let cur = n
            while (list.has(cur)) {
                curlen++
                cur++
            }

            ret = Math.max(ret, curlen)
        }

        return ret
    }
}
