class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const hashset = new Map();

        for (const letter of s) {
            if (hashset.has(letter)) {
                hashset.set(letter, hashset.get(letter) + 1)
            } else {
                hashset.set(letter, 1)
            }
        }

        for (const letter of t) {
            if (hashset.has(letter)) {
                hashset.set(letter, hashset.get(letter) - 1);
                if (hashset.get(letter) === 0) {
                    hashset.delete(letter);
                }
            } else {
                return false;
            }
        }
        if (hashset.size > 0) {
            return false;
        }
        return true;
    }
}
