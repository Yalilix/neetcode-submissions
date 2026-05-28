class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const res = {};
        for (let s of strs) {
            const count = new Array(26).fill(0);
            console.log(count)
            for (let c of s) {
                count[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
            }
            console.log(count)
            const key = count.join(',');
            console.log(key)
            if (!res[key]) {
                res[key] = [];
            }
            res[key].push(s);
        }
        return Object.values(res);
    }
}