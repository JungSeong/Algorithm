#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        deque<pair<string, int>> dq;
        unordered_map<string, bool> visited;
        visited[startGene] = false;
        dq.push_back({startGene, 0});

        for (const auto& b : bank) {
            visited[b] = false;
        }

        while (!dq.empty()) {
            auto [cur, answer] = dq.front();
            visited[cur] = true;
            dq.pop_front();

            if (cur == endGene) {
                return answer;
            }

            for (const auto next : bank) {
                if (!visited[next]) { // visited 되지 않은 bank에 대해서만
                    int cnt = 0;
                    bool isPossible = false;

                    for (int i=0; i<8; i++) {
                        if (cur[i] != next[i]) {
                            cnt++;
                        }
                    }

                    if (cnt == 1) {
                        isPossible = true;
                    }

                    if (isPossible) {
                        dq.push_back({next, answer+1});
                    }
                }
            }
        }

        return -1;
    }
};