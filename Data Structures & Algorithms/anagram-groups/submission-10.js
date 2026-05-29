class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hm = {}
        for (const s of strs) {
            const count = new Array(26).fill(0)
            for (const c of s) {
                count[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
            }

            const key = count.join(',')
            if (!hm[key]) {
                hm[key] = []
            }
            hm[key].push(s)
        }
        return Object.values(hm)
     }
}
