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


       
a = [3,0,1]
b = [0,1]
c = [9,6,4,2,3,5,7,0,1]

print(missingNumber(a))
print(missingNumber(b))
print(missingNumber(c))

# x = {0, 1, 3}
# y = {0, 1, 2, 3}
# print(y-x)