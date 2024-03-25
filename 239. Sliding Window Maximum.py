class Solution:
    '''
    APPROACH-1: BRUTE FORCE
    TIME: O(K * (N - K))
    TLE 37/51
    '''
    # 0 1 2 3 4 5 6
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     res = []
    #     for i in range(n - k + 1):                  # O(N - K)
    #         res.append(max(nums[i : i + k]))            # O(K)
    #     return res


    '''
    APPROACH-1: MONOTONIC DECREASING QUEUE
    TIME: O(N)

    Q will store idx of nums in a decreasing sequence
    traverse i/p
    if curr_val is greater than q.right, keep popping till curr_val < q.right
    add curr_val to q

    if l points to an idx which is greater than q.left => remove q.left

    if l and r are window_size apart, output.append(q.left) => move l (i.e don't move l until they're window size apart)
    
    move r
    
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # left of deq will store the max for a curr_window
        deq = collections.deque()     # stores [val, idx], no need to store val, i'm just doing it for my understanding
        val, idx = 0, 1               # for accessing [val, idx] in deq
        start, right_end = 0, -1
        out = []

        l, r = 0, 0

        while r < len(nums):
            curr_val = nums[r]

            # check if smaller values than curr_val exists, if it does => keep popping
            while deq and deq[right_end][val] < curr_val:
                deq.pop()
            
            # add to deq [val, idx]
            deq.append([curr_val, r])

            # check if l went beyond the idx present at start of deq (i.e. if window moved and there's still a max from previous window)
            # remove it
            if l > deq[start][idx]:
                deq.popleft()

            # if the l and r are window_len apart => add max to output
            window_size = r - l + 1
            if window_size == k:
                out.append(deq[start][val])
                l += 1
            r += 1

        return out
