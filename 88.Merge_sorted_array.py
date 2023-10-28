from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## APPROACH-1: using in built function after copying values from nums2 to nums1
        # fill up zeros in n1 with n2
        # for j in range(n):
        #     nums1[m+j] = nums2[j]

        # nums1.sort()


        ## APPROACH-2: 2 pointers, start filling from end of array
        ## T(N): O(N)
        ## Space: O(1)
        last = len(nums1) - 1

        # while there are still elements in any array
        while m > 0 and n > 0:
            # if val at nums2 is greater
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            # if val at nums1 is greater
            elif nums1[m - 1] >= nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1

        # fill nums1 with left over nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

        print(nums1)




    # BELOW CODE DOESN'T WORK BUT AN HONEST TRY
    # i, j = 0, 0
    # a, b = nums1, nums2

    # if n!= 0:
    #     for _ in range(m+n):
           
    #         # traversed all elements from 1st array
    #         if a[i] == 0:
    #             a[i] = b[j]
    #             i+=1
    #             j+=1
    #         elif i == m+n-1:
    #             break
    #         # element in first array is smaller than element in second array
    #         # simply move the pointer to next element
    #         elif a[i] <= b[j]:
    #             i+=1
    #         # element in first array is bigger than element in second array
    #         # copy the element in second array to first array
    #         else:
    #             a[i+1] = a[i]
    #             a[i] = b[j]
    #             i+=1
    #             j+=1

    # print(a,b)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# # nums1, nums2 = [1], []
# # m, n = 1, 0


# # nums1, nums2 = [0], [1]
# # m, n = 0, 1

# nums1, nums2 = [2,0], [1]
# m, n = 1, 1
s = Solution()
s.merge(nums1, m, nums2, n)