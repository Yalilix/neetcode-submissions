class Solution {
public:

    string encode(vector<string>& strs) {
        string ret = "";

        for (const auto& s : strs) {
            ret += to_string(s.size()) + '#' + s;
        }

        return ret;
    }

    vector<string> decode(string s) {
        vector<string> ret;

        int l = 0;
        while (l < s.size()) {
            int r = l + 1;
            while (s[r] != '#') {
                r++;
            }

            int length = stoi(s.substr(l, r - l));

            l = r + 1;
            string cur = s.substr(l, length);
            ret.push_back(cur);

            l += length;
        }

        return ret;
    }
};
