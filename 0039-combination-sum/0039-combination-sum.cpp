#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> answer;
    vector<unordered_map<int, int>> cnt_map;

    void dfs(int sum, int target, vector<int>& possible, vector<int>& candidates) {
        if (sum > target) {
            return;
        }
        else if (sum == target) {
            unordered_map<int, int> um;

            for (int i : possible) {
                um[i]++;
            }

            for (const auto& dict : cnt_map) {
                if (um == dict) {
                    return;
                }
            }
            cnt_map.push_back(um);
            answer.push_back(possible);
            return;
        }
        else {
            for (const int cand : candidates) {
                possible.push_back(cand);
                dfs(sum+cand, target, possible, candidates);
                possible.pop_back();
            }
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> possible;
        dfs(0, target, possible, candidates);

        return answer;
    }
};