#include <bits/stdc++.h>

class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> visited(nums.size(), false); 
        deque<pair<int, int>> dq;
        dq.push_back({0, 0});
        visited[0] = true;

        while (!dq.empty())
        {
            int idx = dq.front().first;
            int cnt = dq.front().second;
            
            if (idx == nums.size()-1)
            {
                return cnt;
            }
            dq.pop_front();
            int num = nums[idx];

            for (int j=1; j<=num; j++)
            {
                if (idx+j<nums.size() and !visited[idx+j])
                {
                    dq.push_back({idx+j, cnt+1});
                    visited[idx+j] = true;
                }
            }
        }

    return 0;
    }
};