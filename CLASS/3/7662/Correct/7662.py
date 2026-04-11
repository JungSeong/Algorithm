import sys
import heapq as hq
input = sys.stdin.readline

T = int(input())

for t in range(T) :
    K = int(input())
    max_q, min_q = [], []
    cnt = {}

    for k in range(K) :
        ch, n = input().split()
        n = int(n)

        if ch == "I" :
            hq.heappush(min_q, n)
            hq.heappush(max_q, -n)
            cnt[n] = cnt.get(n, 0) + 1
        else :
            if not cnt:
                continue
            if n == -1:  # 최솟값 삭제
                while min_q and cnt.get(min_q[0], 0) == 0 :
                    hq.heappop(min_q)
                if min_q :
                    val = hq.heappop(min_q)
                    cnt[val] -= 1
                    if cnt[val] == 0:
                        del cnt[val]
            else:  # 최댓값 삭제
                while max_q and cnt.get(-max_q[0], 0) == 0 :
                    hq.heappop(max_q)
                if max_q :
                    val = -hq.heappop(max_q)
                    cnt[val] -= 1
                    if cnt[val] == 0:
                        del cnt[val]

    if not cnt :
        print("EMPTY")
    else :
        possible = list(cnt.keys())
        print(f"{max(possible)} {min(possible)}")