#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> arr; // num, idx
        vector<int> answer;
        for (int i=0; i<nums.size(); i++) {
            arr.push_back({nums[i], i});
        }

        sort(arr.begin(), arr.end());
        int start = 0;
        int end = arr.size()-1;
        int left = -1;
        int right = -1;

        while (start < end) {
            left = arr[start].first;
            right = arr[end].first;
            
            int total = left + right;
            if (total == target) {
                answer.push_back(arr[start].second);
                answer.push_back(arr[end].second);
                return answer;
            }
            else if (total < target) {
                start++;
            }
            else {
                end--;
            }
        }

        return answer;
    }
};