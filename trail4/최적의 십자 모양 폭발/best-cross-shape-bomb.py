n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# Please write your code here.
for i in range(n) :
    for j in range(n) :
        temp = [[0]*n for _ in range(n)]
        num = grid[i][j]
        num -= 1

        for c in range(n) :
            cnt = n-1
            for r in range(n-1, -1, -1) :
                if (c==j and i-num<=r<=i+num) or (r==i and j-num<=c<=j+num) :
                    continue
                else :
                    temp[cnt][c] = grid[r][c] 
                    cnt -= 1

        ct = 0

        for r in range(n) :
            for c in range(n-1) :
                if temp[r][c] != 0 :
                    if temp[r][c] == temp[r][c+1] :
                        ct +=1
        
        for r in range(n-1) :
            for c in range(n) :
                if temp[r][c] != 0 :
                    if temp[r][c] == temp[r+1][c] :
                        ct += 1
         
        answer = max(answer, ct)

print(answer)