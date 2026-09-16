#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> answer;

    void dfs(int n, int k, vector<int>& cur) {
        if (cur.size() == k) {
            answer.push_back(cur);
            return;
        }

        int start = 1;
        if (!cur.empty()) {
            start = cur.back()+1;
        }

        for (int i=start; i<=n; i++) {
            cur.push_back(i);
            dfs(n, k, cur);
            cur.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<int> cur;
        dfs(n, k, cur);

        return answer;
    }
};