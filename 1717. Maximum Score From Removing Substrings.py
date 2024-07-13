class Solution:
    '''
         #  
    cdbc[a[ba]a][a[ba]b]
                      #
    cdbcab
    5 + 5 + 5 + 4

    abba => 9

               #    
    cdbcab
    b
    a
    15
           #          
    cdbc

    bbbaaa
    bbaa
    aabb => bbaa
    
    5 + 4


    abbaxyzbaab
    
    disappear like in candy crush

        *
    aacbb
    bbaa
    b a 


    aabbaaxybbaabb




    max_points = 5
    {
        ab : 4
        ba : 5
        
    }

    '''
    '''
    Approach:   2 pass solution
                Take out the higher score substring first
                then lower score substring
    Time: O(N)
    Space: O(N) 
    '''
    def remove_substring(self, org_string: str, substring: str, score: int) -> str:
        curr_total = 0
        start, end = substring[0], substring[1]
        stack = []
        
        for char in org_string:
            if char == end and stack and stack[-1] == start:
                stack.pop()
                curr_total += score
            else:
                stack.append(char)
        
        return (curr_total, "".join(stack))

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            low_scr_substring, high_scr_substring = "ab", "ba"
            low_scr, high_scr = x, y
        else:
            low_scr_substring, high_scr_substring = "ba", "ab"
            low_scr, high_scr = y, x

        # remove high_scr substring
        score_1, processed_substring = self.remove_substring(s, high_scr_substring, high_scr)
        
        # remove low_scr substring
        score_2, processed_substring = self.remove_substring(processed_substring, low_scr_substring, low_scr)

        return score_1 + score_2      # can use a global variable as well

    '''
    Approach: Keeping Count
    say ab has more score
    then for every b encountered when count_a >= 0, decrement count and update score

    for a,b just (remaining), take min of count_a, count_b and product with its cost and update score
    reset count_a, count_b if encounter anythin else
    
               #
    cdbcbbaaabab
    start_count = 1
    end_count = 1
    
    Time: O(n)
    Space: O(1)
    '''
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score, start_count, end_count = 0, 0, 0

        # decide the rule
        # x: ab, y: ba
        if x < y:
            low, high = x, y
            subs_start, subs_end = "b", "a"
        else:
            low, high = y, x
            subs_start, subs_end = "a", "b"

        for char in s:
            if char == subs_end:
                if start_count:
                    start_count -= 1
                    score += high
                else:
                    end_count += 1
            elif char == subs_start:
                start_count += 1    
            else:
                score += min(start_count, end_count) * low
                start_count, end_count = 0, 0

        score += min(start_count, end_count) * low
        return score
