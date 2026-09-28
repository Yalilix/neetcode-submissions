class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;

        int ret = 0;

        while (l < r) {
            int curH = min(heights[l], heights[r]);
            ret = max(ret, curH * (r - l));
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return ret;
    }
};
