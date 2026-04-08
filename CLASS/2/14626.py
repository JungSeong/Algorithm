import sys

input = sys.stdin.readline

ISBN = input().rstrip()
checksum = int(ISBN[-1])
idx = -1
add = 0

for i in range(12):
    if ISBN[i] == '*':
        idx = i
    else:
        if i % 2 == 0:
            add += int(ISBN[i]) * 1
        else:
            add += int(ISBN[i]) * 3

for i in range(10):
    if idx % 2 == 0:
        if (add + checksum + i * 1) % 10 == 0:
            print(i)
    else:
        if (add + checksum + i * 3) % 10 == 0:
            print(i)