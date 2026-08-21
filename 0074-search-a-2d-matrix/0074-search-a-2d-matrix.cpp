#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();

        int left = 0;
        int right = m*n-1;

        int mid = (left+right)/2;
        int mid_r = 0;
        int mid_c = 0;

        while (left <= right) {
            mid = (left+right)/2;
            mid_r = mid/n;
            mid_c = mid%n;

            if (matrix[mid_r][mid_c] == target) {
                return true;
            }
            else if (matrix[mid_r][mid_c] < target) {
                left = mid+1;
            }
            else {
                right = mid-1;
            }
        }

        return false;
    }
};