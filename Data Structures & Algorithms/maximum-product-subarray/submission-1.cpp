class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int ret = nums[0];
        int curMin = 1, curMax = 1;

        for (int n : nums) {
            if (n == 0) {
                curMin = 1; curMax = 1;
                ret = max(ret, 0);
                continue;
            }

            int temp = curMin * n;
            curMin = min({n * curMin, n * curMax, n});
            curMax = max({temp, n * curMax, n});

            ret = max(ret, curMax);
        }

        return ret;
    }
};
