class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hq
        hq.heapify(nums)
        it = len(nums)-k
        for i in range(it) :
            hq.heappop(nums)

        return hq.heappop(nums)