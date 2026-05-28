class Solution {
    /**
     * @param {number} a
     * @param {number} b
     * @return {number}
     */
    getSum(a, b) {
        while (b != 0) {
            const tmp = a
            a = a ^ b
            b = (tmp & b) << 1
        }
        return a
    }
}
