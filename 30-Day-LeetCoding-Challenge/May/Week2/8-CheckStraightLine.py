"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the
coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
"""

class Solution:
    def getGradient(self, p1, p2):
        change_y = p2[1]-p1[1]
        change_x = p2[0]-p1[0]
        if change_y == 0 or change_x == 0:
            return 0
        else:
            return change_y/change_x

    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        gradient = self.getGradient(coordinates[0], coordinates[1])
        for i in range(len(coordinates)-1):
            if gradient != self.getGradient(coordinates[i], coordinates[i+1]):
                return False
        return True



solution = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
res = solution.checkStraightLine(coordinates)
print(res)
