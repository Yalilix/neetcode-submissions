class Solution {
public:
    int countSubstrings(string s) {
        /* 
            dp way:
            - 
        
        
        */
        int n = s.size();
        int ret = 0;
        vector<vector<bool>> dp(n + 1, vector<bool>(n + 1, false));

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])) {
                    dp[i][j] = true;
                    ret++;
                }
            }
        }

        return ret;
    }
};
