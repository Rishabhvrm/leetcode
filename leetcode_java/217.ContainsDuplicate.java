package leetcode_java;

import java.util.HashSet;
import java.util.Set;

class ContainsDuplicate {
    public static void main(String[] args) {
        ContainsDuplicate obj = new ContainsDuplicate();
        int [] arr = {1,2,3,4,5,2};
        System.out.println(obj.containsDuplicate(arr));
    }
    
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        // for(int i = 0; i < nums.length; i ++) {
        //     if (seen.contains(nums[i])) {
        //         return true;
        //     } else {
        //         seen.add(nums[i]);
        //     }
        // }
        for (int n : nums) {
            if (!seen.contains(n)) {
                seen.add(n);
            } else {
                return true;
            }
        }
        return false;
    }
}





