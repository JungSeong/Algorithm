import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())
min_val, max_val = min(X, Y), max(X, Y)

case1 = (X+Y) * W
case2 = min_val * S + (abs(min_val-X) + abs(min_val-Y)) * W

if (X+Y)%2 == 0 :
    case3 = max_val * S
else :
    case_3 = (max_val-1)*S + W

print(min(case1, case2, case3))