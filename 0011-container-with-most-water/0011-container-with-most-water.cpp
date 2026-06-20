#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int answer = -1;

        while (left<right) {
            int mh;
            mh = (height[left] < height[right]) ? height[left] : height[right];
            answer = max(answer, mh*(right-left));

            if (mh == height[left]) {
                left++;
            }
            else {
                right--;
            }
        }

        return answer;
    }
};