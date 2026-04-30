class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        ans = 0
        length = len(s)
        cur = 0

        while cur < length :
            if cur+1 < length :
                k = s[cur] + s[cur+1]
                if k in m.keys() :
                    ans += m[k]
                    cur += 2
                else :
                    ans += m[s[cur]]
                    cur += 1
            else :
                ans += m[s[cur]]
                cur += 1

        print(ans)
        return ans