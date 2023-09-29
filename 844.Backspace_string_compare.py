def backspaceCompare(s: str, t: str) -> bool:
    stack_s, stack_t = [], []

    ## T(N): O(N)
    ## Space Complexity: O(N)
    
    ## APPROACH: 
    ## traverse both lists, 
    ## add on stack, 
    ## remove ele if found #, 
    ## compare at the end

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

    ## APPROACH 2: 2 POINTERS

    p1 = len(s) - 1
    p2 = len(t) - 1
    while p1 >= 0 or p2 >= 0:
        if (p1 >= 0 and s[p1] == '#') or (p2 >= 0 and t[p2] == '#'):
            if p1 >= 0:
                p1 -= 1
            if p2 >= 0:
                p2 -= 1
        elif (p1 >= 0 and p2 >= 0 and s[p1] == t[p2]):
            p1 -= 1
            p2 -= 1
        else:
            return False

    return True

    



# s = "ab##"
# t = "c#d#"
# print(backspaceCompare(s,t))

# s = "y#fo##f"
# t = "y#f#o##f"
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s,t))