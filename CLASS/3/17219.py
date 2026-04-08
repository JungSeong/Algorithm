import sys

input = sys.stdin.readline

N, M = map(int, input().split())
d = {}

for i in range(N):
    address, password = input().split()
    d[address] = password

for j in range(M):
    name = input().rstrip()
    print(d[name])