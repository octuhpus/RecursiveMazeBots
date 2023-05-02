import sys
import cv2

from src.Controller import Controller
from src.RecursiveBacktrackingMaze import Backtracking

sys.setrecursionlimit(8000)


def main():

    # Uses (y, x) format. Use y = 4 for blank example
    myMaze = Backtracking(25, 25)     # both params must be > 4

    mazeController = Controller(myMaze.maze, myMaze.width, myMaze.height)
"""
    # maze example
    exampleMaze = Backtracking(50, 50)

    cv2.namedWindow('ExampleMaze', cv2.WINDOW_NORMAL)
    cv2.resizeWindow("ExampleMaze", 500, 500)
    cv2.imshow('ExampleMaze', exampleMaze.maze)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""

if __name__ == "__main__":
    main()
