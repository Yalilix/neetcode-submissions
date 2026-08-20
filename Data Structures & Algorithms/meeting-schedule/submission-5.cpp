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
        vector<pair<int, int>> meetings;
        for (auto [s, e] : intervals) {
            meetings.emplace_back(s, e);
        }

        sort(meetings.begin(), meetings.end());
        int end = -1;
        for (int i = 0; i < meetings.size(); i++) {
            int s = meetings[i].first;
            int e = meetings[i].second;

            if (s < end) return false;
            end = e;
        }

        return true;
    }
};
