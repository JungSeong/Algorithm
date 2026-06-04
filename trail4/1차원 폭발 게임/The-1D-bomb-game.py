n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
while True :
    start, cnt = 0, 1
    explodes = [False]*len(numbers)

    for i in range(1, len(numbers)) :
        if numbers[i] == numbers[i-1] :
            cnt += 1
        else :
            if cnt >= m :
                for j in range(start, i) :
                    explodes[j] = True
            start = i
            cnt = 1
        
    if cnt >= m :
        for j in range(start, len(numbers)) :
            explodes[j] = True

    isOK = True
    for e in explodes :
        if e :
            isOK = False
            break

    if isOK :
        break

    temp = []
    for i in range(len(explodes)) :
        if not explodes[i] :
            temp.append(numbers[i])

    numbers[:] = temp

print(len(numbers))
if numbers :
    for e in numbers :
        print(e)