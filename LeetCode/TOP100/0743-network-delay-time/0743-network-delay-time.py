class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        
        m = defaultdict(list)
        for u, v, w in times :
            m[u].append((v, w))

        visited = [False]*(n+1)
        answer = [float('inf')]*(n+1)

        import heapq as hq
        heap = []
        hq.heappush(heap, (0, k))
        answer[k] = 0        

        while heap :
            dist, node = hq.heappop(heap)
            if visited[node] :
                continue
            visited[node] = True

            for v, w in m[node] :
                new_dist = dist + w
                answer[v] = min(answer[v], new_dist)
                hq.heappush(heap, (new_dist, v))

        if max(answer[1:]) == float('inf') :
            return -1
        else :
            return max(answer[1:])