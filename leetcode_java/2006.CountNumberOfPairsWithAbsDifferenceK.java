package leetcode_java;

import java.util.HashMap;

class Test {
    public static void main(String[] args) {
        System.out.println(new Solution().countKDifference(new int[] {1,2,2,1}, 1));
    }
}

class Solution {
    public int countKDifference(int[] nums, int k) {
        int count = 0;
        HashMap<Integer, Integer> freq = new HashMap<>();

        // count occurance of each number
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        for (int num : freq.keySet()) {
            if (freq.keySet().contains(num + k)) {
                count += freq.get(num) * freq.get(num + k);
            }
        }
        return count;
    }
}