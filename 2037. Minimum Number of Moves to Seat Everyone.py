from typing import List
class Solution:
    '''
    Approach-1: counting sort + using stack
    make arrangement arr (pic below)
    make stacks for chairs and students
    compare tops and calculate moves

        S   S     S 
      C   C   C
    _ _ _ _ _ _ _ _ 
    0 1 2 3 4 5 6 7

    Time: O(n + N), N: max val in seats or students
    '''
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        stud_stack, seat_stack, moves = [], [], 0

        N = max(max(seats), max(students)) + 1
        arrangement = [[i] for i in range(N)]

        for s in seats:
            arrangement[s].append("seat")

        for s in students:
            arrangement[s].append("stud")

        for ele in arrangement:
            if len(ele) > 1:
                for c in ele:
                    if c == "seat":
                        seat_stack.append(ele)
                    if c == "stud":
                        stud_stack.append(ele)
            
            while seat_stack and stud_stack:
                a, b = seat_stack.pop(), stud_stack.pop()
                moves += abs(a[0] - b[0])

        return moves
        
    '''
    Approach-2: GREEDY, using sorting
    assign the lowest student to lowest chair and move on
    Time: O(n * log n)
    '''
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = 0
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])

        return moves

    '''
    Approach-3: counting sort + unmatched (counting steps)
    
    [3, 1, 5], [2, 7, 4]
    1: chair, -1: students

    _,1,-1,1,-1,1,_,-1 
    
    0 1  2 3  4 5 6  7

    Time: O(n + N), N: max val in seats or students
    '''
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        N = max(max(seats), max(students))
        diff = [0] * (N + 1)
        moves, unmatched = 0, 0

        for s in seats:
            diff[s] += 1
        
        for s in students:
            diff[s] -= 1

        for d in diff:
            moves += abs(unmatched)
            unmatched += d
        
        return moves

    '''
    Approach: counting sort + 2 arrays
 
    [3, 1, 5]    0 1 0 1 0 1 0 0
    [2, 7, 4]    0 0 1 0 1 0 0 1 
    idx          0 1 2 3 4 5 6 7

    Time: O(n + N), N: max val in seats or students
    '''
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_count = [0] * (max(seats) + 1)
        students_count = [0] * (max(students) + 1)

        for s in seats:
            seats_count[s] += 1
        
        for s in students:
            students_count[s] += 1

        i, j = 0, 0
        moves = 0
        remaining_studs = len(students)
        
        # while i < len(seats_count) or j < len(students_count):
        while remaining_studs:
            if seats_count[i] == 0:
                i += 1

            if students_count[j] == 0:
                j += 1

            if seats_count[i] and students_count[j]:
                moves += abs(j - i)
                seats_count[i] -= 1
                students_count[j] -= 1
                remaining_studs -= 1

        return moves