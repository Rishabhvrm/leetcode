from typing import List
import heapq

class Solution:
    '''
    APPROACH-1: Using hashmap (counter) and sorting
    store the occurance of each ele in map
    sort the map
    return top k values
    TIME: O(N * log N)
    SPACE: O(N)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = {}        # {ele -> its occurance}
        for n in nums: counter[n] = counter.get(n, 0) + 1                       # store occurances
        
        # sort hashmap according to values (occurances)
        # [(1, 3), (2, 2), (3, 1)]
        sorted_counter_list = sorted(counter.items(), key = lambda x : x[1], reverse=True)  
        
        for i in range(k): res.append(sorted_counter_list[i][0])                # pick top k keys 
        return res
    
    '''
    APPROACH-2: Using hashmap (counter) and heap
    store the occurance of each ele in map
    put the map on heap ( O(n) )
    pop top k values    ( O(k * log n))
    TIME: O(K * log N), 
    SPACE: O(N)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = {}        # {ele -> its occurance}
        for n in nums: counter[n] = counter.get(n, 0) + 1  # store occurances
        
        hp = []                                            # add (occurance, ele) values to heap
        for i in counter.keys():
            if len(hp) == k:                               # limiting heap size to k, push before pop
                heapq.heappush(hp, (counter[i], i))        # push (occurance, ele) on min-heap, heap rearranges
                heapq.heappop(hp)                          # pop the min-value so that only greater values stays on heap
            else:
                heapq.heappush(hp, (counter[i], i))        # freely push on heap
        
        while hp:
            res.append(heapq.heappop(hp)[1])                # heap will contain k values, pop and add to result
        
        return res
    
    '''
    APPROACH-3: Using hashmap (counter) and buckets
    store each ele on the bucket where bucket's idx = ele's occurance
    TIME: O(N), 
    SPACE: O(N)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]        # make (n + 1) buckets
        counter = {}                                        # {ele -> its occurance}
        for n in nums: counter[n] = counter.get(n, 0) + 1   # store occurances
        
        # add elements to buckets => filling the buckets
        for ele, occurance in counter.items():
            buckets[occurance].append(ele)

        # traversing the buckets in reverse order because we want the top k
        for bucket in reversed(buckets):                    
            for ele in bucket:
                res.append(ele)
                if len(res) == k: return res

        # for i in range(len(buckets) - 1, 0, -1):
        #     for ele in buckets[i]:
        #         res.append(ele)
        #         if len(res) == k: return res

