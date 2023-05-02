import numpy as np
import random
import Enums as ens


class Backtracking:

    def __init__(self, height, width):

        if width % 2 == 0:
            width += 1
        if height % 2 == 0:
            height += 1

        self.maze = np.ones((height, width), dtype=float)
        self.width = width
        self.height = height
        self.createMaze()

    def createMaze(self):

        for i in range(self.height):
            for j in range(self.width):
                if i % 2 == 1 or j % 2 == 1:
                    self.maze[i, j] = 0
                if i == 0 or j == 0 or i == self.height - 1 or j == self.width - 1:
                    self.maze[i, j] = 0.5

        sx = random.choice(range(2, self.width - 2, 2))
        sy = random.choice(range(2, self.height - 2, 2))

        self.generator(sx, sy, self.maze)

        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i, j] == 0.5:
                    self.maze[i, j] = 1

    def generator(self, cx, cy, grid):
        grid[cy, cx] = 0.5

        if grid[cy - 2, cx] == 0.5 and grid[cy + 2, cx] == 0.5 and grid[cy, cx - 2] == 0.5 and grid[cy, cx + 2] == 0.5:
            pass
        else:
            li = [1, 2, 3, 4]
            while len(li) > 0:
                dir = random.choice(li)
                li.remove(dir)

                if dir == ens.Direction.UP.value:
                    ny = cy - 2
                    my = cy - 1
                elif dir == ens.Direction.DOWN.value:
                    ny = cy + 2
                    my = cy + 1
                else:
                    ny = cy
                    my = cy

                if dir == ens.Direction.LEFT.value:
                    nx = cx - 2
                    mx = cx - 1
                elif dir == ens.Direction.RIGHT.value:
                    nx = cx + 2
                    mx = cx + 1
                else:
                    nx = cx
                    mx = cx

                if grid[ny, nx] != 0.5:
                    grid[my, mx] = 0.5
                    self.generator(nx, ny, grid)
