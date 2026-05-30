n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
arr = l+r+d
arr[:] = arr[-t%(3*n):] + arr[:-t%(3*n)]

print(" ".join(map(str, arr[:n])))
print(" ".join(map(str, arr[n:2*n])))
print(" ".join(map(str, arr[2*n:3*n])))