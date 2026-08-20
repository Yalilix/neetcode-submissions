class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (int i = 0; i < edges.size(); i++) {
            int s = edges[i][0];
            int t = edges[i][1];
            graph[s].push_back(t);
            graph[t].push_back(s);
        }

        set<int> visited;
        if (!dfs(0, -1, graph, visited)) return false;
        return visited.size() == n;
    }

private:
    bool dfs(int i, int parent, vector<vector<int>>& graph, set<int>& visited) {
        if (visited.contains(i)) return false;

        visited.insert(i);
        for (auto nei : graph[i]) {
            if (nei == parent) continue;
            cout << nei << i << endl;
            if (!dfs(nei, i, graph, visited)) return false;
        }

        return true;
    }
};
