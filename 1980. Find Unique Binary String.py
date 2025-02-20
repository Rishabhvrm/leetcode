from typing import List
class Solution:
    # find n
    # generate all possible binary strings of len n
    # as you generate, return the first one that doesn't exist in nums_set = set(nums)
    # def findDifferentBinaryString(self, nums: List[str]) -> str:

    #     def generate_all_possible_strs(curr):
    #         if len(curr) == n and curr not in nums_set:
    #             return curr
            
    #         if len(curr) == n:
    #             return ""
            
    #         add_zero = generate_all_possible_strs(curr + "0")
            
    #         curr.append(0)


    #     n = len(nums[0])
    #     nums_set = set(nums)
    #     return generate_all_possible_strs("")

    '''
    convert into decimal
    store in set
    check from 0 to 2 ^ n - 1, return the first number that is absent in set
    convert to binary before returning
    '''
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        def dec_to_binary(decimal, length):
            return bin(decimal)[2:].zfill(length)

        num_set = set(int(num, 2) for num in nums)
        n = len(nums)
        decimal = -1

        for i in range(pow(2, n)):
            if i not in num_set:
                decimal = i
                break

        return dec_to_binary(decimal, n)