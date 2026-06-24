#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        vector<pair<int, int>> n;
        for (int i=0; i<nums.size(); i++) {
            n.push_back({nums[i], i});
        }

        sort(n.begin(), n.end());

        for (int i=1; i<n.size(); i++) {
            if (n[i].first == n[i-1].first && abs(n[i].second - n[i-1].second) <= k) {
                return true;
            }
        }

        return false;
    }
};