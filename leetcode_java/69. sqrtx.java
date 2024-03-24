package leetcode_java;

class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        int l = 1, r = x;
        int ans = -1;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            
            if (mid == x / mid) {
                return mid;
            }
            else if (x / mid < mid) {
                r = mid - 1;
            }
            else if (mid < x / mid) {
                ans = mid;
                l = mid + 1;
            }
        }

        return ans;
    }
}