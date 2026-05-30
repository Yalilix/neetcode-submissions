class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0
        let r = s.length - 1

        while (l < r) {
            let left = s[l].toLowerCase()
            while (!((left >= 'a' && left <='z') || (left >= '0' && left <='9')) && l < r) {
                l++              
                left = s[l].toLowerCase()  
            }

            let right = s[r].toLowerCase()
            while (!((right >= 'a' && right <='z') || (right >= '0' && right <='9')) && l < r) {
                r--
                right = s[r].toLowerCase()
            }


            if (s[l].toLowerCase() !== s[r].toLowerCase()) { 
                return false
            }

            l++
            r--
        }

        return true

    }
}
