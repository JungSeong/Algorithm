#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        int n = 1;
        int answer = 0;

        while(n<=x/n) {
            if (n*n <= x) {
                answer = max(answer, n);
                n++;
            }
            else {
                break;
            }
        }

        return answer;
    }
};