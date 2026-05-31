class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const hm = { "}": "{", "]": "[", ")": "("}
        const stack = []

        for (let i = 0; i < s.length; i++) {
            if (hm[s[i]] === undefined) {
                stack.push(s[i])
            } else {
                if (stack.pop() === hm[s[i]]) continue 
                return false
            }
        }
        return stack.length === 0
    }   
}
