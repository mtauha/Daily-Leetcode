"""Description:
  Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

  Implement KthLargest class:
  
      KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
      int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.stream) < self.k or self.stream[0] < val:
            heapq.heappush(self.stream, val)
            if len(self.stream) > self.k:
                heapq.heappop(self.stream)
        return self.stream[0]


sol = KthLargest("""Enter Variables Here""")
