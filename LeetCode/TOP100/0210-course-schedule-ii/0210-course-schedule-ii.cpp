#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> indegree;
    unordered_map<int, vector<int>> graph;

    vector<int> answer(int n) {
        queue<int> q;
        vector<int> answer;

        for (int i=0; i<n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int Node = q.front();
            q.pop();
            answer.push_back(Node);

            for (const auto next : graph[Node]) {
                indegree[next]--;

                if (indegree[next] == 0) {
                    q.push(next);
                }
            }
        }

        if (answer.size() != n) {
            return {};
        }

        return answer;
    }

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int N = prerequisites.size();
        indegree.assign(numCourses, 0);

        for (const auto& item : prerequisites) {
            int from = item[1];
            int to = item[0];

            indegree[to]++;
            graph[from].push_back(to);
        }

        return answer(numCourses);
    }
};