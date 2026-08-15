#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_map<char, int> m;
        for (const auto& jewel : jewels) {
            m[jewel] = 1; 
        }
        int answer = 0;

        for (const auto& stone : stones) {
            if (m[stone]) { // 처음 호출하면 m[stone]=0 == False로 생성이 됨, 위와 같이 하여 m[stone]==1 == True임을 검증
                answer++;
            }
        }

        return answer;
    }
};