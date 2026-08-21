class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);

        for (auto& edge : edges) {
            int s = edge[0];
            int t = edge[1];

            graph[s].push_back(t);
            graph[t].push_back(s);
        }

        int count = 0;
        set<int> seen;

        for (int i = 0; i < n; i++) {
            if (!seen.contains(i)) {
                dfs(i, graph, seen);
                count++;
            }
        }

        return count;
    }

private:
    void dfs(int node, vector<vector<int>>& graph, set<int>& seen) {
        if (seen.contains(node)) return;
        seen.insert(node);
        for (auto nei : graph[node]) {
            dfs(nei, graph, seen);
        }
    }
};
