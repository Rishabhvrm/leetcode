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
    for ele in s:
        if ele == "#":
            if stack_s: stack_s.pop() 
        else: stack_s.append(ele)

    # add elements of t on stack
    for ele in t:
        if ele == "#":
            if stack_t: stack_t.pop()
        else: stack_t.append(ele)

    # return true if both equal else false
    return stack_s == stack_t


# s = "ab##"
# t = "c#d#"
# print(backspaceCompare(s,t))

s = "y#fo##f"
t = "y#f#o##f"
print(backspaceCompare(s,t))