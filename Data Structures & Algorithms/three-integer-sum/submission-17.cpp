class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        int n = nums.size();
        vector<vector<int>> ret;

        for (int i = 0; i < n; i++) {
            int num1 = nums[i];

            if (i > 0 and num1 == nums[i - 1]) continue; 

            int l = i + 1, r = n - 1;

            while (l < r) {
                int sum = num1 + nums[l] + nums[r];

                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    ret.push_back({num1, nums[l], nums[r]});
                    l++;
                    
                    while (l < r and l - 1 >= 0 and nums[l - 1] == nums[l]) {
                        l++;
                    }
                }
            }
        }

        return ret;
    }
};
