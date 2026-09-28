class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        map<char, char> mp = {
            {']', '['},
            {'}', '{'},
            {')', '('}
        };


        for (auto c : s) {
            if (!mp.contains(c)) {
                stk.push(c);
            } else {
                if (!stk.empty() and stk.top() == mp[c]) {
                    stk.pop();
                } else {
                    return false;
                }
            }
        }

        return stk.empty() ? true : false;
    }
};
