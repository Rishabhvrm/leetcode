package leetcode_java;

class TrappingRainWater {
    public static void main(String[] args) {
        System.out.println(trap(new int[] {0,1,0,2,1,0,1,3,2,1,2,1}));
        System.out.println(trap(new int[] {4,2,0,3,2,5}));
    }

    public static int trap(int[] height) {
        int l = 0, r = height.length - 1, trappedWater = 0;

        // max height values for l and r pointers
        int lMax = height[l], rMax = height[r];

        while (l < r) {
            if (lMax < rMax) {
                l += 1;                                 // move l
                lMax = Math.max(lMax, height[l]);       // update lMax
                trappedWater += lMax - height[l];       // update trappedWater
            } else {
                r -= 1;                                 // move r
                rMax = Math.max(rMax, height[r]);       // update lMax
                trappedWater += rMax - height[r];       // update trappedWater
            }
        }

        return trappedWater;
    }
}
