#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (const auto& ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                st.push(ch);
            }
            else {
                if (st.size() != 0) {
                    if (st.top() == '(' && ch == ')' || st.top() == '[' && ch == ']' || st.top() == '{' && ch == '}') {
                        st.pop();
                    }
                    else {
                        return false;
                    }
                }
                else {
                    return false;
                }
            }
        }

        if (st.size() == 0) {
            return true;
        }
        else {
            return false;
        }
    }
};