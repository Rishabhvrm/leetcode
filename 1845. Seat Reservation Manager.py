from collections import heapq
class SeatManager:

    def __init__(self, n: int):
        self.min_heap = [i for i in range(1, n + 1)]        # unreserved seats
        heapq.heapify(self.min_heap)
        self.reserved = [False for i in range(n + 1)]       # reserved seats

    def reserve(self) -> int:
        idx = heapq.heappop(self.min_heap)
        self.reserved[idx] = True
        return idx        

    # can also use a hashset
    def unreserve(self, seatNumber: int) -> None:
        self.reserved[seatNumber] = False
        heapq.heappush(self.min_heap, seatNumber)
