A = input()
ans = float('inf')

# Please write your code here.
for a in range(len(A)) :
    A = str(A[-1]) + A[:-1]
    st = ""
    cnt = 1

    for n in range(1, len(A)) :
        if A[n] == A[n-1] :
            cnt += 1
        else :
            st += (A[n-1]+str(cnt))
            cnt = 1
    
    st += (A[-1]+str(cnt))
    ans = min(ans, len(st))

print(ans)