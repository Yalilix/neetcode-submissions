class KthLargest {
    int lim;
    priority_queue<int, vector<int>, greater<int>> pq;
public:
    KthLargest(int k, vector<int>& nums) {
        lim = k;
        for (auto n : nums) {
            pq.push(n);
            if (pq.size() > k) pq.pop();
        }
    }
    
    int add(int val) {
        pq.push(val);
        if (pq.size() > lim) pq.pop();
        return pq.top();
    }
};
