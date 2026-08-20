#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double answer = 0;

        for (int i=0; i<k; i++) {
            answer += nums[i];
        }
        answer /= k;
        double comp = answer;

        for (int i=1; i<=nums.size()-k; i++) {
            comp = (comp*k-nums[i-1]+nums[i+k-1])/k;

            if (answer < comp) {
                answer = comp;
            }
        }
        return answer;
    }
};