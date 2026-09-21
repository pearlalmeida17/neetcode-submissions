import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # Transform array into a Min-Heap in O(N) time
        heapq.heapify(self.heap)
        
        # Keep only the top k largest elements
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Push the new value onto the heap
        heapq.heappush(self.heap, val)
        
        # If the size exceeds k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root (smallest in top-k) is the k-th largest overall
        return self.heap[0]