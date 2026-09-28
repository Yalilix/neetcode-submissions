class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> mp;

        for (string s : strs) {
            mp[getKey(s)].push_back(s);
        }

        vector<vector<string>> ret;
        for (auto [_, v] : mp) {
            ret.push_back(v);
        }

        return ret;
    }

private: 
    string getKey(string s) {
        int count[26] = {0};

        for (char c : s) {
            count[c - 'a']++;
        }

        string t;
        for (int c = 0; c < 26; c++) {
            t += string(count[c], c + 'a') + '#';
        }

        return t;
    }
};
