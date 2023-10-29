from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        ## APPROACH-1: BRUTE FORCE
        ## TIME: O(M + N), but have to do in log(m+n)
        ## SPACE: O(M + N)

        # i, j = 0, 0
        # arr = []

        # # merge 2 arrays into arr[]
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] <= nums2[j]:
        #         arr.append(nums1[i])
        #         i += 1
        #     else:
        #         arr.append(nums2[j])
        #         j += 1
        
        # # add remaining elements
        # arr.extend(nums1[i:])
        # arr.extend(nums2[j:])


        # # find median      
        # l = len(arr)
        # if l % 2 != 0:              # if l is odd
        #     median = arr[l//2]
        # else:                       # if l is even
        #     median = (arr[l//2] + arr[l//2 - 1]) / 2

        # return median



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
            # partition in B is from starting till half - i
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





# nums1 = [1,2]
# nums2 = [3,4]     # works
nums1 = [1,3]
nums2 = [2]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))