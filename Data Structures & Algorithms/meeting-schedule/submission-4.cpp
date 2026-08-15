/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        vector<pair<int, int>> revInt;
        for (auto [s, e] : intervals) {
            revInt.emplace_back(e, s);
        }

        sort(revInt.begin(), revInt.end());
        int prevEnd = -1;
        for (auto [e, s] : revInt) {
            if (s < prevEnd) return false;
            prevEnd = e;
        }
        return true;
    }
};
