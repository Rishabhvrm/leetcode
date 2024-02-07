package leetcode_java.fundamentals_java;

public class BinarySearch {
    public static void main(String[] args) {
        System.out.println(binarySearch(new int[] {1,2,3,4,5}, 3));
        System.out.println(binarySearch(new int[] {1,2,3,4,5}, 0));
    }

    public static int binarySearch(int [] nums, int target) {
        int l = 0, r = nums.length;

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) l = mid + 1;       // discard left-half
            else if (target < nums[mid]) r = mid - 1;       // discard right-half
        }
        return - 1;
    }
}
