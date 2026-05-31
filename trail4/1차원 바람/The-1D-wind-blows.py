n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def move(r, loc) :
    if loc == "L" :
        a[r][:] = [a[r][-1]] + a[r][:-1]
    else :
        a[r][:] = a[r][1:] + [a[r][0]]

# Please write your code here.
for r, loc in winds :
    r = r-1
    move(r, loc)
    left, right = r-1, r+1
    
    while True :
        if loc == "L" :
            loc = "R"
        else :
            loc = "L"

        lposs, rposs = False, False

        if 0 <= left :
            for i in range(m) :
                if a[left][i] == a[left+1][i] :
                    lposs = True
                    break
                    
        if right < n :
            for i in range(m) :
                if a[right][i] == a[right-1][i] :
                    rposs = True
                    break

        if lposs :
            move(left, loc)
            left -= 1
        if rposs :
            move(right, loc)
            right += 1
        if not lposs and not rposs :
            break

for row in a :
    print(" ".join(map(str, row)))