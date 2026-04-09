import sys, math
input = sys.stdin.readline

n = int(input())
comments = []

if n == 0 :
    print(0)
    exit(0)

for i in range(n) :
    comments.append(int(input()))

comments.sort()
p = n*0.15
p = int(p+0.5)
answer = 0

if p == 0 :
    answer = sum(comments)
else :
    answer = sum(comments[p:-p])

answer /= (n-p*2)
answer = int(answer+0.5)
print(answer)