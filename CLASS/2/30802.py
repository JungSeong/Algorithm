import sys

input = sys.stdin.readline

N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())
ans1 = 0

for s in shirts:
    ans1 += s // T
    ans1 += 1 if s % T != 0 else 0

print(ans1)
print(f"{N // P} {N % P}")