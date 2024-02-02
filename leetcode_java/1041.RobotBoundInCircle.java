package leetcode_java;

class Test {
    public static void main(String[] args) {
        System.out.println(RobotBoundInCircle.isRobotBounded("GG"));
    }
}

class RobotBoundInCircle{
    public static boolean isRobotBounded(String instructions) {
        // directions: North - 0, East - 1, South - 2, West - 3
        int x = 0, y = 0, direction = 0;

        for (char cmd : instructions.toCharArray()) {
            if (cmd == 'G') {
                if (direction == 0) { y += 1; }          // move up in y-axis
                else if (direction == 1) { x += 1; }     // move right in x-axis
                else if (direction == 2) { y -= 1; }     // move down in y-axis
                else if (direction == 3) { x -= 1; }     // move left in x-axis
            }
            // turning left means moving to the previous direction in direction array
            else if (cmd == 'L') {
                direction = (direction + 3) % 4;
            }
            // turning right means moving to the next direction in direction array
            else if (cmd == 'R') {
                direction = (direction + 1) % 4;
            }
        }
        // if robot ends up at the same place where it started 
        // OR
        // if it's not facing as the initial direction
        // it'll stay in circles
        return (x == 0 && y == 0) || direction != 0;
    }
}