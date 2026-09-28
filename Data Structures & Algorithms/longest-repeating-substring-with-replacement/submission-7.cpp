class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0, r = 0;
        map<char, int> mp;

        int ret = 0;
        while (r < s.size()) {
            mp[s[r]]++;
            int maxCount = max_element(mp.begin(), mp.end(), [](auto& a, auto& b){
                return a.second < b.second;
            })->second;

            while ((r - l + 1) - maxCount > k) {
                mp[s[l]]--;
                l++;
                maxCount = max_element(mp.begin(), mp.end(), [](auto& a, auto& b){
                    return a.second < b.second;
                })->second;
            }

            ret = max(ret, r - l + 1);
            r++;
        }

        return ret;
    }
};
