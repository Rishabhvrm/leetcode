from typing import List
class Solution:
    '''
                #
    5,5,5,5,10,20,10
    5: 3
    10: 1
    20: 1

    20

    Approach: simulation w/ hashmap, greedy: use 10s first
    Time: O(N)
    Space: O(1), constant space of hashmap, only 3 keys ever

    for every 10 or 20 add to map, and check in the map if it has 5 or 15, 
        if yes, update the map and move ahead
        else: return False
    while removing, I have to take care to remove 10s first not 5s
    '''
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_freq = defaultdict(int)

        for b in bills:
            if b == 10:
                if bill_freq[5] >= 1:
                    bill_freq[5] -= 1
                else:
                    return False
            if b == 20:
                curr_10s = 10 * bill_freq[10]
                curr_5s = 5 * bill_freq[5]
                total_money = curr_10s + curr_5s
                if total_money < 15:
                    return False
                else:
                    # can I make 15?
                    if curr_10s >= 1 and curr_5s >= 1:
                        bill_freq[10] -= 1
                        bill_freq[5] -= 1
                    elif curr_5s >= 3:
                        bill_freq[5] -= 3
                    else:
                        return False
            bill_freq[b] += 1

        return True
    '''
    Approach: simulation w/o hashmap, greedy: use 10 first
    Time: O(N)
    Space: O(1)
    '''
    def lemonadeChange(self, bills: List[int]) -> bool:
        fd_bill = td_bill = 0
        
        for b in bills:
            if b == 5:
                fd_bill += 1
            elif b == 10:
                # check if you can give 5 back
                if fd_bill >= 1:
                    fd_bill -= 1
                    td_bill += 1
                else:
                    return False
            elif b == 20:
                # check if you can give 15 back (either 5 * 3 or 5 + 10)
                if td_bill >= 1 and fd_bill >= 1:
                    td_bill -= 1
                    fd_bill -= 1
                elif fd_bill >= 3:
                    fd_bill -= 3
                else:
                    return False

        return True