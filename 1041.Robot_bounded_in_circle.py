class Solution:
    # returns True if robot stays in the circle
    def isRobotBounded(self, instructions: str) -> bool:
        
        # directions: North - 0, East - 1, South - 2, West - 3
        x, y, direction = 0, 0, 0
        for cmd in instructions:
            if cmd == "G":
                if direction == 0: y += 1           # move up y-axis
                elif direction == 1: x += 1         # move right x-axis     
                elif direction == 2: y -= 1         # move down y-axis
                elif direction == 3: x -= 1         # move left x-axis
            # anticlockwise, go
            # turning left means moving to the previous direction in the directions array
            elif cmd == "L":
                direction = (direction + 3) % 4
            # turning right means moving to the next direction in the directions array
            elif cmd == "R":
                direction = (direction + 1) % 4

        # robot makes a circle if it is back where it started or it's not facing north
        return (x == 0 and y == 0) or direction != 0


sol = Solution()
print(sol.isRobotBounded("GR"))