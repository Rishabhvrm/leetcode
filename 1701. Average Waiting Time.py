from typing import List
class Solution:
    '''
    having trouble implementing. Finding the overlap
        > was able to code it up correctly in one try. Just implemented what I drew the picture of

    -----
    1 2 3 4 5 6 7 8 9 10 11
    '''
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        overlap, total, end_time_for_prev_cust = 0, 0, 0

        for arrrival_t, t_needed in customers:
            if arrrival_t < end_time_for_prev_cust:
                overlap = end_time_for_prev_cust - arrrival_t 
                total += overlap
            
            total += t_needed
            end_time_for_prev_cust = arrrival_t + overlap + t_needed

        return (total)/len(customers)


    '''
    same concept as above, coded differently
    '''
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wt_time, curr_time = 0, 0

        for arrival_time, cook_time in customers:
            if curr_time < arrival_time:
                curr_time = arrival_time

            total_wt_time += curr_time + cook_time - arrival_time
            curr_time += cook_time
        
        return total_wt_time / len(customers)