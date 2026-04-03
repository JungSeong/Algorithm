import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, 2*N) :
    if i < N :
        print(" "*(i-1), end="*"*(2*(N-i)+1))
        print()
    else :
        print(" "*(2*N-i-1), end="*"*(2*(i-N)+1))
        print()