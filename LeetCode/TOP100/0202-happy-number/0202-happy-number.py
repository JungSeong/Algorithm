class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True :
            if n != 1 :
                print("test")
                print(n)
                if n not in seen :
                    seen.add(n)
                    n = sum(int(x)**2 for x in str(n))
                else :
                    return False
            else :
                print(n)
                return True