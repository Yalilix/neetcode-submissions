class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let ret = ""

        for (const s of strs) {
            ret += s.length + "#" + s
        } 
        
        return ret
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let ret = []
        let i = 0
        while (i < str.length) {
            let j = i
            while (str[j] != "#") {
                j++
            }

            let len = parseInt(str.substring(i, j))
            i = j + 1
            j = i + len
            
            ret.push(str.substring(i, j))
            i = j
        }

        return ret
    }
}
