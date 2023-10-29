# similar to 448. Find all numbers disappeared in an Array
def missingNumber(nums) -> int:    
    n = len(nums)

    # convert the list to set to use set subtraction
    first_set = set(nums)
    
    # second set stores all the numbers from 0 to n
    second_set = set()
    for ele in range(n+1):
        second_set.add(ele)
    
    # use set subtraction to find the missing value (or difference)
    return (second_set - first_set).pop()

    ## APPROACH-2: USING LIST AND SET
    # revision
def missing_number(nums) -> int:
    s = set()
    # create set to store all numbers
    for x in range(len(nums)+1):
        s.add(x)
    
    # traverse input list and remove those element from set
    for ele in nums:
        s.remove(ele)
    
    # only the missing number should remain in the set, return that
    return s.pop()


       
a = [3,0,1]
b = [0,1]
c = [9,6,4,2,3,5,7,0,1]

print(missingNumber(a))
print(missingNumber(b))
print(missingNumber(c))

# x = {0, 1, 3}
# y = {0, 1, 2, 3}
# print(y-x)