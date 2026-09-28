class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ret;
        
        int cur = 1;
        for (auto n : nums) {
            ret.push_back(cur);
            cur *= n;
        }

        // 1, 1, 2, 8
        // 48, 24, 6, 1

        cur = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            ret[i] *= cur;
            cur *= nums[i];
        }

        return ret;
    }
};
