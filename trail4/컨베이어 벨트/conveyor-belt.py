n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
tot = u + d
ans = [0]*2*n

for i in range(2*n) :
    ans[(i+t)%(2*n)] = tot[i]

print(" ".join(map(str, ans[:n])))
print(" ".join(map(str, ans[n:])))