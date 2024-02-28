package leetcode_java;

class Solution {
    public boolean isPowerOfThree(int n) {
        int num = n;
        if (num < 1) return false;
        while (num % 3 == 0) {
            num = num / 3;
        }
        return num == 1;
    }
}