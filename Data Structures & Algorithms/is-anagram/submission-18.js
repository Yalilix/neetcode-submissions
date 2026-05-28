class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) return false

        const hm1 = {}
        const hm2 = {}

        for (let i = 0; i < s.length; i++) {
            hm1[s[i]] = 1 + (hm1[s[i]] || 0)
            hm2[t[i]] = 1 + (hm2[t[i]] || 0)
        }

        for (const c in hm1) {
            if (hm1[c] !== hm2[c]) {
                return false
            }
        }

        return true
    }
}
