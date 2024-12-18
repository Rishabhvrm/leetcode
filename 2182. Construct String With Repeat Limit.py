from collections import defaultdict
import heapq
class Solution:
    '''
    cczazcc 3
    zzcccacc
    cczzacc 

    aabbcc
    cbcba
    cbacba
    '''
    '''
    at first seemed pretty hard
    was able to find the solution using hints
    but couldn't code it

    lesson: 
        state machine, automata
        was using seek instead of pop
        was confused about how to add it back if pop was used
        was confused about the condition for while loop, should it be i, should it be max_heap size?
        was right about storing the ascii value in heap but didn't store the count in heap itself, was going to map for it


        if count - curr_count > 0 and chars_heap: 
        this is very counterintuitive, almost like couldn't come up with it if didn't know
        to move to the next char, we're checking if the occurances of curr one are available
    '''
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = []
        char_occ = defaultdict(int)
        
        for c in s:
            char_occ[c] += 1
            
        chars_max_heap = [(-ord(c), count) for c, count in char_occ.items()]
        heapq.heapify(chars_max_heap)
        
        while chars_max_heap:
            char, count = heapq.heappop(chars_max_heap)
            char = chr(-char)
            
            curr_count = min(count, repeatLimit)
            res.append(char * curr_count)
            new_count = count - curr_count
            
            if new_count > 0 and chars_max_heap:
                nxt_char, nxt_count = heapq.heappop(chars_max_heap)
                nxt_char = chr(-nxt_char)
                res.append(nxt_char)
                new_nxt_count = nxt_count - 1
                
                if new_nxt_count > 0:
                    heapq.heappush(chars_max_heap, (-ord(nxt_char), new_nxt_count))
            
                heapq.heappush(chars_max_heap, (-ord(char), new_count))
            
        
        return "".join(res)