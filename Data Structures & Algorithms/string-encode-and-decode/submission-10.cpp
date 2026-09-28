class Solution {
public:

    string encode(vector<string>& strs) {
        string ret;
        for (auto s : strs) {
            ret += to_string(s.size()) + '#' + s;
        }
        return ret;
    }

    vector<string> decode(string s) {
        int i = 0;
        vector<string> ret;

        while (i < s.size()) {
            int j = i + 1;
            while (s[j] != '#') {
                j++;
            }

            int len = stoi(s.substr(i, j - i));
            i = j + 1;
            ret.push_back(s.substr(i, len));
            i += len;
        }

        return ret;
    }
};
