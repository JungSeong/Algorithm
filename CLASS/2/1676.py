import sys
input = sys.stdin.readline

N = int(input())
factorial = 1

for i in range(2, N+1) :
    factorial *= i

factorial = str(factorial)
answer = 0

for i in range(len(factorial)-1, -1, -1) :
    if factorial[i] == '0' :
        answer += 1
    else :
        break

print(answer)