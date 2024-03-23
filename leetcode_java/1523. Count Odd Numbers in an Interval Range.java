package leetcode_java;

class Solution {
    /*
    APPROACH-1: traverse low to high and check each number
    */
    public int countOdds(int low, int high) {
        int oddCount = 0;
        for (int i = low; i <= high; i++) {
            if (i % 2 != 0){
                oddCount ++;
            }
        }
        return oddCount;
    }

    /*
    APPROACH-2: is there a better way?
    for any range of numbers, half would be even and half would be odd
    [1,2,3] => len = 3 => odd numbers = 2
    [0,1,2] => len = 3 => odd numbers = 1
    
    [1,2,3,4] => len = 4 => odd count = 2
    [2,3,4,5] => len = 4 => odd count = 2

    if len is even, it would always be half odd + half even
    if len is odd, then it depends on the boundaries
        if the boundaries are odd, then odd count is ceil(half) 
        if the boundaries are even, then odd count is floor(half)
    */
    public int countOdds2(int low, int high) {
        int length = high - low + 1;
        int oddCount = length / 2;          // this is the ans for even length

        // check if length is odd and one of the boundaries is odd => add 1 based on above example/logic
        if (length % 2 != 0 && low % 2 != 0){
            oddCount++;
        }
        return oddCount;
    }
}