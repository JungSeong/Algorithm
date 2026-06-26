#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> answer;

        for (int i=0; i<nums.size()-2; i++) {
            if (i>0 && nums[i] == nums[i-1]) {
                continue;
            }
            int fix = nums[i];
            int start = i+1;
            int end = nums.size()-1;
            int total = 0;

            while (start < end) {
                total = fix + nums[start] + nums[end];

                if (total == 0) {
                    vector<int> v = {nums[i], nums[start], nums[end]};
                    bool isOK = true;

                    if (isOK) {
                        answer.push_back(v);
                    }

                    start++;
                    end--;

                    while (start < end && start > 0 && nums[start] == nums[start-1]) {
                        start++;
                    }

                    while (start < end && end < nums.size()-1 && nums[end] == nums[end+1]) {
                        end--;
                    }
                }
                else if (total < 0) {
                    start++;
                }
                else {
                    end--;
                }
            }
        }

        return answer;
    }
};