class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) return false;

        const hash1 = {}
        const hash2 = {}
        
        for (const i in s) {
            hash1[s[i]] = 1 + (hash1[s[i]] || 0);
            hash2[t[i]] = 1 + (hash2[t[i]] || 0);
        }

        for (const key in hash1) {
            if (hash1[key] !== hash2[key]) {
                return false;
            }
        }
        return true;
    }   
}
