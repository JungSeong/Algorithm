n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

for n in range(2) :
    s = 0
    temp = [0]*len(blocks)
    for j in range(len(blocks)) :
        if n==0 and not s1-1<=j<=e1-1 or n==1 and not s2-1<=j<=e2-1 :
            temp[s] = blocks[j]
            s+=1
    blocks[:] = temp

if len(blocks)==0 :
    print("0")
else :
    while blocks :
        if blocks[-1] == 0 :
            blocks.pop()
        else :
            break
    
    print(len(blocks))
    for e in blocks :
        print(e)