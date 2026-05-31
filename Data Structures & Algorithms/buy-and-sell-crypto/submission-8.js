class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l = 0
        let ret = 0

        for (let r = 0; r < prices.length; r++) {
            if (prices[r] < prices[l]) {
                l = r
            } else {
                ret = Math.max(ret, prices[r] - prices[l])
            }
        }
        return ret
    }
}
