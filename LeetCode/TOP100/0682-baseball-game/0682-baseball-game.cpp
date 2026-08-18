#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int calPoints(vector<string>& operations) {
        deque<int> dq;

        for (const auto& oper : operations) {
            int n = dq.size();
            if (oper == "+") {
                dq.push_back(dq[n-1]+dq[n-2]);
            }
            else if (oper == "D") {
                dq.push_back(dq[n-1]*2);
            }
            else if (oper == "C") {
                dq.pop_back();
            }
            else {
                dq.push_back(stoi(oper));
            }
        }

        int answer = 0;
        for (const auto& num : dq) {
            answer += num;
        }

        return answer;
    }
};