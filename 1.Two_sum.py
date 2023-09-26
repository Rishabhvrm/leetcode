def twoSum(nums, target):
    result, l = [], len(nums)
    i= 0
    while i < l:
        j = i + 1
        while j < l:
            second_num = target - nums[i]
            if nums[j] == second_num:
                result.append(i)
                result.append(j)
                return result
            j += 1
        i += 1

    return result

n1, t1 = [2,7,11,15], 9
n2, t2 = [3,2,4], 6
n3, t3 = [3,3], 6

print(twoSum(n1,t1))
print(twoSum(n2,t2))
print(twoSum(n3,t3))
