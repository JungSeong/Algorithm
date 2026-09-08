#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    unordered_map<int, vector<int>> graph;
    vector<int> state; // 아직 방문하지 않은 상태로 초기화

    bool dfs(int cur) {
        if (state[cur] == 1) { // 이미 방문한 노드를 재방문
            return false;
        }

        if (state[cur] == 2) { // 이미 안전을 확인한 노드를 방문
            return true;
        }

        state[cur] = 1;
        for (int next : graph[cur]) {
            if (!dfs(next)) { // 이미 방문한 노드를 또 방문했다면
                return false;
            }
        }
        
        state[cur] = 2;
        return true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        state.assign(numCourses, 0);

        for (const auto& nodes : prerequisites) {
            int cur = nodes[0];
            int pre = nodes[1];

            graph[pre].push_back(cur);
        }

        for (int course=0; course<numCourses; course++) {
            if (state[course] == 0) { // 아직 방문하지 않은 노드인 경우
                if (!dfs(course)) {
                    return false;
                }
            }
        }

        // for (const auto& [k, v] : graph) {
        //     cout << k << ' ';
        //     for (const auto& next : v) {
        //         cout << next << endl;
        //     }
        // }

        return true;
    }
};