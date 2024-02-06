package leetcode_java;

class Solution {
    // ## Approach-1: simulate the robot's position after each move
    // ## Time: O(n)
    // ## Space: O(n), charArray
    public boolean judgeCircle(String moves) {
        int x = 0, y = 0;
        for (char c : moves.toCharArray()) {
            if (c == 'U') y += 1;
            else if (c == 'D') y -= 1;
            else if (c == 'L') x -= 1;
            else if (c == 'R') x += 1;
        }
        return x == 0 && y == 0;
    }
}