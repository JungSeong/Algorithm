class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hq
        heap = []

        for i in range(len(nums)) :
            hq.heappush(heap, -nums[i])

        for i in range(k) :
            p = heapq.heappop(heap)
            
            if i == k-1 :
                return -p