#include <bits/stdc++.h>
using namespace std;

class Solution {
    int row = 0;
    int col = 0;
    vector<vector<bool>> visited;
    vector<pair<int, int>> dirs{
        {-1, 0}, {0, 1}, {1, 0}, {0, -1}
    };

    vector<pair<int, int>> capture(
        int r,
        int c,
        const vector<vector<char>>& board
    ) {
        deque<pair<int, int>> dq;
        vector<pair<int, int>> region;
        bool surrounded = true;

        dq.push_back({r, c});
        visited[r][c] = true;

        while (!dq.empty()) {
            auto [cur_r, cur_c] = dq.front();
            dq.pop_front();

            region.push_back({cur_r, cur_c});

            // 영역의 O가 하나라도 경계에 있으면 포획할 수 없다.
            if (cur_r == 0 || cur_r == row - 1 ||
                cur_c == 0 || cur_c == col - 1) {
                surrounded = false;
            }

            for (const auto& [dr, dc] : dirs) {
                int new_r = cur_r + dr;
                int new_c = cur_c + dc;

                if (new_r < 0 || new_r >= row ||
                    new_c < 0 || new_c >= col) {
                    continue;
                }

                if (board[new_r][new_c] == 'O' &&
                    !visited[new_r][new_c]) {
                    visited[new_r][new_c] = true;
                    dq.push_back({new_r, new_c});
                }
            }
        }

        return surrounded ? region : vector<pair<int, int>>{};
    }

public:
    void solve(vector<vector<char>>& board) {
        if (board.empty() || board[0].empty()) {
            return;
        }

        row = board.size();
        col = board[0].size();
        visited.assign(row, vector<bool>(col, false));

        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (board[i][j] != 'O' || visited[i][j]) {
                    continue;
                }

                vector<pair<int, int>> surrounded =
                    capture(i, j, board);

                for (const auto& [r, c] : surrounded) {
                    board[r][c] = 'X';
                }
            }
        }
    }
};