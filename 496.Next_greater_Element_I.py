from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ## APPROACH-1: Brute force,
        # for every element in n1, find its idx in n2
        # and check if any element greater than that exists
        # to the right of it
        ## TIME: O ( n * n ), traversing n1, traversing n2 for each ele in n1; index()
        ## SPACE: O (n), output array
        res = []
        for i in nums1:
            start = nums2.index(i)
            find_flag = False
            for j in range(start + 1, len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    find_flag = True
                    break
            if not find_flag: res.append(-1)

        return res
    
    def nextGreaterElement2(self, nums1, nums2):
        # Create a stack to keep track of elements
        stack = []
        # Create a dictionary to store the next greater elements
        next_greater = {}

        # Iterate through nums2 from right to left
        for num in nums2:
            # While the stack is not empty and the current element is greater than the top of the stack
            while stack and stack[-1] < num:
                # Pop elements from the stack and mark their next greater element as the current element
                next_greater[stack.pop()] = num
            # Push the current element onto the stack
            stack.append(num)
        # Iterate through nums1 to get the corresponding next greater elements
        result = [next_greater.get(num, -1) for num in nums1]
        return result
    
    def nextGreaterElement3(self, nums1, nums2):
        stack = []
        dic = {}
        for n in nums2:
            while stack and stack[-1] < n:
                dic[stack.pop()] = n
            stack.append(n)

        res = []
        for n in nums1:
            if n in dic:
                res.append(dic[n])
            else:
                res.append(-1)                

        return res
            


    
obj = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
# print(obj.nextGreaterElement(nums1, nums2))
print(obj.nextGreaterElement3(nums1, nums2))