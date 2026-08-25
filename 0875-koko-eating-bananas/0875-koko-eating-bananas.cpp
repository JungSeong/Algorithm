#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        long long H = 0;
        int answer=1;
        sort(piles.begin(), piles.end());

        int start = 1;
        int end = piles.back();
        int mid = -1;

        while (start <= end) {
            mid = (start+end)/2;
            H = 0;
            for (const auto& pile : piles) {
                H += pile/mid + (pile%mid != 0);
            }

            if (H > h) {
                start = mid+1;
            }
            else {
                end = mid-1;
                answer = mid;
            }
        }

        return answer;
    }
};