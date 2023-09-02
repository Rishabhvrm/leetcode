def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # fill up zeros in n1 with n2
    for j in range(n):
        nums1[m+j] = nums2[j]

    nums1.sort()
    print(nums1)

#     i, j = 0, 0
#     a, b = nums1, nums2

#     if n!= 0:
#         for _ in range(m+n):
           
#             # traversed all elements from 1st array
#             if a[i] == 0:
#                 a[i] = b[j]
#                 i+=1
#                 j+=1
#             elif i == m+n-1:
#                 break
#             # element in first array is smaller than element in second array
#             # simply move the pointer to next element
#             elif a[i] <= b[j]:
#                 i+=1
#             # element in first array is bigger than element in second array
#             # copy the element in second array to first array
#             else:
#                 a[i+1] = a[i]
#                 a[i] = b[j]
#                 i+=1
#                 j+=1

#     print(a,b)


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# # nums1, nums2 = [1], []
# # m, n = 1, 0


# # nums1, nums2 = [0], [1]
# # m, n = 0, 1

nums1, nums2 = [2,0], [1]
m, n = 1, 1

merge(nums1, m, nums2, n)