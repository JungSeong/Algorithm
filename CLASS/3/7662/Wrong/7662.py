import sys
import heapq as hq
input = sys.stdin.readline

T = int(input())
for t in range(T) :
    K = int(input())
    q = []

    for k in range(K) :
        ch, n = input().split()
        n = int(n)
        hq.heapify(q)

        if ch == "I" :
            hq.heappush(q, n)
        else :
            if q:
                if n == -1 :
                    hq.heappop(q)
                else :
                    q = list(map(lambda x : -x, q))
                    hq.heapify(q)
                    hq.heappop(q)
                    q = list(map(lambda x : -x, q))

    if not q :
        print("EMPTY")
    else :
        print(f"{max(q)} {min(q)}")