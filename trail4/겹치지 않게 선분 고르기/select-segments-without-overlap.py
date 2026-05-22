n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
sel = []

def DFS(idx, cnt) :
    if idx == n :
        return cnt

    answer = DFS(idx+1, cnt)
    isSel = False

    for s, e in sel :
        if x2[idx] < s or x1[idx] > e :
            continue
        else :
            isSel = True
            break
    if not isSel :
        sel.append([x1[idx], x2[idx]])
        answer = max(answer, DFS(idx+1, cnt+1))
        sel.pop()

    return answer

print(DFS(0, 0))