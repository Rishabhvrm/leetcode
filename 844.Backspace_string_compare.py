class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        
        ## APPROACH 1: 
        ## traverse both lists, 
        ## add on stack, 
        ## remove ele if found #, 
        ## compare at the end

        ## T(N): O(N)
        ## Space Complexity: O(N)

        # add elements of s on stack
        # for ele in s:
        #     if ele == "#":
        #         if stack_s: stack_s.pop() 
        #     else: stack_s.append(ele)

        # # add elements of t on stack
        # for ele in t:
        #     if ele == "#":
        #         if stack_t: stack_t.pop()
        #     else: stack_t.append(ele)

        # # return true if both equal else false
        # return stack_s == stack_t

        ## APPROACH 2
        ## 2 POINTERS

        # # set pointers to point end 
        # i, j = len(s) - 1, len(t) - 1

        # # move pointers from back to front
        # while i >= 0 or j >= 0:

        #     # Skip any backspace characters in both strings
        #     while i >= 0 and s[i] == '#':
        #         i -= 1                          # skip '#'
        #         if i >= 0: i -= 1               # move to previous element of '#'
            
        #     while j >= 0 and t[j] == '#':
        #         j -= 1
        #         if j >= 0: j -= 1

        #     # return false if any mismatch
        #     if i >= 0 and j >= 0 and s[i] != t[j]: return False

        #     i -= 1
        #     j -= 1

        # # return true if loop is done i.e. no mistmatch found
        # return True

        def get_valid_idx(str, idx):
            # chars to skip
            count_backspace = 0

            while idx >= 0:
                # increase countr if '#' encountered
                if str[idx] == "#": count_backspace += 1

                # skip elemets till counter becomes 0
                elif count_backspace > 0: count_backspace -= 1

                # don't decrease idx if a valid char
                else: break

                # decrease index after every '#' or skip
                idx -= 1
            return idx
        
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            
            i = get_valid_idx(s,i)
            j = get_valid_idx(t,j)

            # compare elements at i and j 
            # if both -1, it means they reached start of array without any mismatch
            # return True
            if i < 0 and j < 0 : return True

            # if mitmatch or one string ended while other still has elements
            # return False
            if i < 0 or j < 0 or s[i] != t[j]: return False

            i -= 1
            j -= 1

        return True
