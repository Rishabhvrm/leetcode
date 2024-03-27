from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        ## APPROACH-1: BRUTE FORCE
        ## TIME: O(M + N), but have to do in log(m+n)
        ## SPACE: O(M + N)

        i, j = 0, 0
        arr = []

        # merge 2 arrays into arr[]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        # add remaining elements
        arr.extend(nums1[i:])
        arr.extend(nums2[j:])


        # find median      
        l = len(arr)
        if l % 2 != 0:              # if l is odd
            median = arr[l//2]
        else:                       # if l is even
            median = (arr[l//2] + arr[l//2 - 1]) / 2

        return median

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## APPROACH-2: BINARY SEARCH AND PARTITION
        ## TIME: O(log(m+n))
        ## SPACE: O(1)

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # pick A to be smaller
        if len(A) > len(B):
            A, B = B, A

        print(f'A: {A}, B: {B}, total: {total}, half: {half}')

        # to find mid of A
        left, right = 0, len(A) - 1
        
        print(f'left: {left}, right: {right}')
        
        while True:
            i = (left + right) // 2     # A, i is mid
            j = half - i - 2            # B, -2 bcz 0 idx
            print(f'i: {i}, j: {j}')

            # partition in A is from starting till i (mid)
            # partition in B is from starting till half - i - 2     ( 0 idx )
            # assign Aleft, Aright, Bleft and Bright
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # check if partition is correct
            print(f'Aleft, Aright, Bleft, Bright: {Aleft, Aright, Bleft, Bright}')
            if Aleft <= Bright and Bleft <= Aright:
                print(f'Aleft <= Bright and Bleft <= Aright: {Aleft <= Bright and Bleft <= Aright}')
                # odd
                if total % 2:
                    return min(Aleft, Bleft)
                # even                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # if partition is incorrect
            # Aleft > Bright => Aleft shouldn't be in partition => move right pointer
            elif Aleft > Bright:
                print(f'Aleft > Bright: {Aleft > Bright}')
                right = i - 1
            # Bleft > Aright => Aright should be in partition => move left pointer   
            else:
                print('else')
                left = i + 1

    def findMedianSortedArrays_revisit(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        t_len = len(nums1) + len(nums2) 
        h_len = t_len // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            a = l + (r - l) // 2
            b = h_len - a - 2           # 0 idx

            # calculate imp points to check partition
            # cover edge cases by initializing values
            A_left = A[a] if a >= 0 else float('-inf')
            A_right = A[a + 1] if (a + 1) < len(A) else float('inf')
            B_left = B[b] if b >= 0 else float('-inf')
            B_right = B[b + 1] if (b + 1) < len(B) else float('inf')

            # check partition
            if A_left <= B_right and B_left <= A_right:
                if t_len % 2:       # odd len
                    return min(A_right, B_right)
                else:               # even len
                    return (min(A_right, B_right) + max(A_left, B_left)) / 2
            # incorrect partition
            elif A_right < B_left:      # include A_right in partition, expand
                l = a + 1
            elif B_right < A_left:      # exclude A_left from partition, shrink
                r = a - 1




# nums1 = [1,2]
# nums2 = [3,4]     # works
nums1 = [1,3]
nums2 = [2]
s = Solution()
# print(s.findMedianSortedArrays(nums1, nums2))
print(s.findMedianSortedArrays_revisit(nums1, nums2))


class Solution2:
    '''
    median will be at middle of merged array
    let's make the left half of this merged array virtually
    for an ideal scenario:
        half of this merged_half would come from (left half of arr1)
        other half of this merged_half would come from (left half of arr2)

    initial partition is decided with the help of mid(of A), in order to find the left half of A
    we take start to mid from smaller array
    and then remaining elements from bigger array (remaining = half - mid)

    if total_length(t) is odd, 
    then left_partition(LP) of the merged_array would contain floor(t/2) elements and 
    right_partition(RP) would contain ceil(t/2) elements
    then, median would be the min(RP)

    if t is even, both LP and RP would contain t/2 elements
    then, median would be the AVG(max(LP), min(RP))

    check if you make the correct partitions by checking
        rightmost val of LP of A < leftmost val of RP of B
        AND
        rightmost val of LP of B < leftmost val of RP of A
    using inf and -inf to handle edge cases
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A         # storing smaller array in A

        total_len = len(nums1) + len (nums2)
        half = total_len // 2

        l, r = 0, len(A) - 1
        while True:
            # make partitions till mid values
            a = l + (r - l) // 2        # mid of A
            b = half - a - 1 - 1        # B, OFF by 1 error: -1 bcz idx starts from 0 for both A and B

            # find 4 values to check if the partition is correct by comapring them 
            # make sure indexes don't go out of bounds by giving default values
            # left denotes mid, i.e. point till partition is considered, 
            # right denotes the element just next to left (just outside the boundary)
            A_left = A[a] if a >= 0 else float('-inf')
            A_right = A[a + 1] if (a + 1) < len(A) else float('inf')
            B_left = B[b] if b >= 0 else float('-inf')
            B_right = B[b + 1]  if (b + 1) < len(B) else float('inf')

            # check if partitions are correct
            if A_left <= B_right and B_left <= A_right:
                if total_len % 2:           # odd length
                    return min(A_right, B_right)
                else:                       # even length
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            # if partitions are not correct
            elif A_right < B_left:      # include A_right and move right (expand the partition)
                l = a + 1
            elif A_left > B_right:      # exclude A_left and move left (shrink the partition)
                r = a - 1


