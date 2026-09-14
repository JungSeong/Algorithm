#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> dict1;
        unordered_map<char, int> dict2;
        bool isPermutationIN = false;
        int cnt = 0;

        if (s1.length() > s2.length()) {
            isPermutationIN = false;
        }
        else {
            for (int i=0; i<s1.length(); i++) {
                dict1[s1[i]]++;
                dict2[s2[i]]++;
            }

            for (int i=s1.length(); i<=s2.length(); i++) {
                cnt = 0;
                for (const auto& [key, val] : dict1) {
                    if (dict1[key] != dict2[key]) {
                        break;
                    }
                    cnt++;
                }
                
                if (cnt == dict1.size()) {
                    isPermutationIN = true;
                    break;
                }

                dict2[s2[i-s1.length()]]--;
                dict2[s2[i]]++;
            }
        }

        return isPermutationIN;
    }
};