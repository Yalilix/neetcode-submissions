class Solution {
   public:
    int longestConsecutive(vector<int>& nums) {
        map<int, int> mp;

        for (auto n : nums) {
            mp[n]++;
        }

        int ret = 0;
        for (auto n : nums) {
            if (mp.contains(n - 1)) continue;

            int cur = n;
            int len = 0;
            while (mp.contains(cur)) {
                len++;
                cur++;
            }
            ret = max(ret, len);
        }

        return ret;
    }
};
