from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # if slope of 2 line segments is not equal => not a straight line

        if len(coordinates) <= 2: return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for coordinate in coordinates:
            x, y = coordinate

            # if slope isn't equal return False
            if (y - y1) * (x2 - x1) != (x - x1) * (y2 - y1): return False

        return True

    # below falis - points doesn't need to be equidistant
    '''
        x_diff = abs(coordinates[0][0]) - abs(coordinates[1][0])
        y_diff = abs(coordinates[0][1]) - abs(coordinates[1][1])
        l = len(coordinates)

        # if line is on x-axis
        count_y = 0
        for i in range(l):
            if coordinates[i][1] == coordinates[0][1]: count_y += 1
        if count_y == l : return True

        # if line is on y-axis
        count_x = 0
        for i in range(l):
            if coordinates[i][0] == coordinates[0][0]: count_x += 1
        if count_x == l : return True

        # if points are equidistant
        for i in range(1, l - 1):
            if x_diff != abs(coordinates[i][0]) - abs(coordinates[i + 1][0]) or \
               y_diff != abs(coordinates[i][1]) - abs(coordinates[i + 1][1]):
               return False

        return True
    '''

c = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
c = [[0,0],[0,1],[0,-1]]
obj = Solution()
print(obj.checkStraightLine(c))