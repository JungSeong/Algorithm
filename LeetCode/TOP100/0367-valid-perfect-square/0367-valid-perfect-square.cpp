#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPerfectSquare(int num) {
        int n = 1;

        while (n <= num/n) {
            if (n*n == num) {
                return true;
            }
            n++;
        }
        return false;
    }
};