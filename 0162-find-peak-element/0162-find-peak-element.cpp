#include <bits/stdc++.h>
using namespace std;

class Solution {
public :
    vector<int> list;
    vector<bool> visited;
    int answer;

    void findElem(int mid) {
        int left = mid-1;
        int right = mid+1;
        visited[mid] = true;

        long long left_elem = (0 <= left) ? list[left] : LLONG_MIN;
        long long right_elem = (right < list.size()) ? list[right] : LLONG_MIN;
        long long mid_elem = list[mid];

        if (left_elem < mid_elem && mid_elem > right_elem) {
            answer = mid;
            return;
        }
        else {
            if (left >= 0 && !visited[left]) {
                findElem(left);
            }
            if (right < list.size() && !visited[right]) {
                findElem(right);
            }
        }
    }

    int findPeakElement(vector<int>& nums) {
        list = nums;
        visited.assign(nums.size(), false);
        findElem(nums.size()/2);

        return answer;
    }
};