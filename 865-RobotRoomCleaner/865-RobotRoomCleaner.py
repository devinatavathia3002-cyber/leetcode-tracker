# Last updated: 2/9/2026, 9:54:33 PM
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        visited = set()

        def moveBack():
            robot.turnRight()
            robot.turnRight()

            robot.move()

            robot.turnRight()
            robot.turnRight()
        
        def dfsExplore(x, y, curr_direction):

            visited.add((x, y))
            robot.clean()

            for i in range(4):
                new_direction = (curr_direction + i) % 4

                new_x = x + directions[new_direction][0]
                new_y = y + directions[new_direction][1] 

                if (new_x, new_y) not in visited and robot.move():
                    dfsExplore(new_x, new_y, new_direction)
                    moveBack()
                
                robot.turnRight()
        
        dfsExplore(0, 0, 0)