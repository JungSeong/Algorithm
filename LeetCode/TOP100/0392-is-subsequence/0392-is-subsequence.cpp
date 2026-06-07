class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0;
        if (s.empty())
        {
            return true;
        }

        for (int j=0; j<t.length(); j++)
        {
            if (s[i] == t[j])
            {
                i += 1;
            }
            if (i == s.length())
            {
                return true;
            }
        }

        return false;
    }
};