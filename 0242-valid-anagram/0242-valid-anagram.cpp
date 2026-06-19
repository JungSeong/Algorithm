#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> ms;
        unordered_map<char, int> mt;

        if (s.size() != t.size()){
            return false;
        }

        for (int i=0; i<s.size(); i++){
            ms[s[i]]++;
            mt[t[i]]++;
        }

        return ms == mt;
    }
};