class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const hm = new Map()
        let len = 0
        let l = 0

        for (let r = 0; r < s.length; r++) {
            hm.set(s[r], 1 + (hm.get(s[r]) || 0))
            
            let curMax = Math.max(...hm.values())

            while ((r - l + 1) - (curMax) > k) {
                hm.set(s[l], hm.get(s[l]) - 1)
                l++

                curMax = Math.max(...hm.values())
            }
            len = Math.max(len, r - l + 1)
        }

        return len
    }
}
