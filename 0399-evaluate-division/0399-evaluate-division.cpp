#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    unordered_map<string, vector<pair<string, double>>> graph;

    double bfs(const string& start, const string& end)
    {
        if (!graph.count(start) || !graph.count(end)) {
            return -1.0;
        }

        if (start == end) {
            return 1.0;
        }

        deque<pair<string, double>> dq;
        unordered_set<string> visited;

        dq.push_back({start, 1.0});
        visited.insert(start);

        while (!dq.empty()) {
            auto [ch, weight] = dq.front();
            dq.pop_front();

            for (const auto& [next, w] : graph[ch]) {
                if (visited.count(next)) {
                    continue;
                }

                double next_weight = weight * w;

                if (next == end) {
                    return next_weight;
                }

                visited.insert(next);
                dq.push_back({next, next_weight});
            }

        }

        return -1.0;
    }

    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        vector<double> answer;

        for (int i=0; i<values.size(); i++)
        {
            graph[equations[i][0]].push_back({equations[i][1], values[i]});
            graph[equations[i][1]].push_back({equations[i][0], 1/values[i]});
        }

        for (const auto& query : queries)
        {
            const string& start = query[0];
            const string& end = query[1];

            answer.push_back(bfs(start, end));
        }

        return answer;
    }
};