#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int find_elem(int left, int right, int target, vector<int>& nums) {
        if (left <= right) {
            int mid = (left+right)/2;
            if (nums[mid] == target) {
                return mid;
            }
            else {
                if (nums[left] <= nums[mid]) { // 왼쪽은 확실히 정렬
                    if (nums[left] <= target && target < nums[mid]) { // 확실히 왼쪽에 있음
                        return find_elem(left, mid-1, target, nums);
                    }
                    else { // 왼쪽에는 확실히 없음
                        return find_elem(mid+1, right, target, nums);
                    }
                }
                else { // 오른쪽은 확실히 정렬
                    if (nums[mid] < target && target <= nums[right]) {
                        return find_elem(mid+1, right, target, nums);
                    }
                    else {
                        return find_elem(left, mid-1, target, nums);
                    }
                }
            }
        }
        else {
            return -1;
        }
    }

    int search(vector<int>& nums, int target) {
        return find_elem(0, nums.size()-1, target, nums);
    }
};