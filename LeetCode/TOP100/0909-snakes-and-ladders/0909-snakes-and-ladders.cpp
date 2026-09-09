#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> reversed;
    vector<vector<bool>> visited;
    int N;

    int bfs(int cur_r, int cur_c, int cnt) {
        deque<tuple<int, int, int>> dq;
        dq.push_back({cur_r, cur_c, cnt});
        visited[cur_r][cur_c] = true;

        while (!dq.empty()) {
            auto [cur_r, cur_c, cnt] = dq.front();
            dq.pop_front();
            int cur_rc = cur_r * N + cur_c;

            if (cur_rc == N*N-1) {
                return cnt;
            }

            for (int move=1; move<=6; move++) {
                int new_rc = cur_rc + move;

                if (new_rc >= N*N) {
                    break;
                }

                int new_r = new_rc / N;
                int new_c = new_rc % N;

                if (reversed[new_r][new_c] != -1) {
                    int dest = reversed[new_r][new_c] - 1;
                    new_r = dest / N;
                    new_c = dest % N;
                }

                if (!visited[new_r][new_c]) {
                    visited[new_r][new_c] = true;
                    dq.push_back({new_r, new_c, cnt+1});
                }
            }
        }

        return -1;
    }

    int snakesAndLadders(vector<vector<int>>& board) {
        reversed = board;
        int n = board.size();
        N = n;

        visited.assign(N, vector<bool>(N, false));

        reverse(reversed.begin(), reversed.end());

        for (int i=0; i<N; i++) {
            if (i%2 == 1) {
                reverse(reversed[i].begin(), reversed[i].end());
            }
        }

        int answer = bfs(0, 0, 0);
        return answer;
    }
};