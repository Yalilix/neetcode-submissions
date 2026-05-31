class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let ret = 0
        
        let l = 0
        let r = heights.length - 1


        while (l < r) {
            const h = Math.min(heights[l], heights[r])

            ret = Math.max(h * (r - l), ret)

            if (heights[l] > heights[r]) {
                r--
            } else {
                l++
            }
        }

        return ret
    }
}
