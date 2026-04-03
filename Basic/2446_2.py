import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(1, 2*N-1) :
    if i < N :
        arr.append(" "*(2*(i-N)+1))
        arr.extend("*"*(2*(N-i)+1))
    else :
        arr.append(" "*(2*(N-i)+1))
        arr.extend("*"*(2*(i-N)+1))
    print(arr)

for elem in arr :
    print(elem)