class Solution:
    import heapq

    def kClosest(self, points, k):
        heap = [(x*x + y*y, x, y) for x, y in points]
        heapq.heapify(heap)  # O(n)
        return [[x, y] for _, x, y in (heapq.heappop(heap) for _ in range(k))]