#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> answer(n, 0);
        stack<int> st;

        for (int i=0; i<n; i++) {
            while (!st.empty() && temperatures[i] > temperatures[st.top()]) { // 아직 더 따뜻한 날을 만나지 못한 인덱스
                answer[st.top()] = i-st.top();
                st.pop();
            }
            st.push(i);
        }

        return answer;
    }
};