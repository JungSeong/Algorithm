#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> answer;

    void dfs(int sum, int target, int start, vector<int>& possible, vector<int>& candidates) {
        if (sum > target) {
            return;
        }
        else if (sum == target) {
            answer.push_back(possible);
            return;
        }
        else {
            for (int i=start; i<candidates.size(); i++) {
                possible.push_back(candidates[i]);
                dfs(sum+candidates[i], target, i, possible, candidates);
                possible.pop_back();
            }
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> possible;
        dfs(0, target, 0, possible, candidates);

        return answer;
    }
};