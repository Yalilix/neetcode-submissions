class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const hm = new Set()

        let l = 0
        let r = l
        let len = 0

        while (r < s.length) {
            while (hm.has(s[r])) {
                hm.delete(s[l])
                l++
            }
            hm.add(s[r])

            len = Math.max(len, r - l + 1)
            r++
        }

        return len
    }
}
