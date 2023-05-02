from Enums import Direction


class MazeBot:
    def __init__(self, maze, lx, ly):
        self.fitness = 0
        self.maze = maze
        self.lx = lx  # location x
        self.ly = ly  # location y
        self.openDir = set()

    # determine what fitness and what directions are open and
    # removes directions that are no longer open
    def determineFitness(self, maze):

        if maze[self.ly - 1, self.lx] == 1 or maze[self.ly - 1, self.lx] == .2:    # up == 1
            self.fitness += 1
            self.openDir.add(Direction.UP)
        elif Direction.UP in self.openDir:
            self.openDir.remove(Direction.UP)

        if maze[self.ly + 1, self.lx] == 1 or maze[self.ly + 1, self.lx] == .2:    # down == 2
            self.fitness += 1
            self.openDir.add(Direction.DOWN)
        elif Direction.DOWN in self.openDir:
            self.openDir.remove(Direction.DOWN)

        if maze[self.ly, self.lx - 1] == 1 or maze[self.ly, self.lx - 1] == .2:    # left == 3
            self.fitness += 1
            self.openDir.add(Direction.LEFT)
        elif Direction.LEFT in self.openDir:
            self.openDir.remove(Direction.LEFT)

        if maze[self.ly, self.lx + 1] == 1 or maze[self.ly, self.lx + 1] == .2:    # right == 4
            self.fitness += 1
            self.openDir.add(Direction.RIGHT)
        elif Direction.RIGHT in self.openDir:
            self.openDir.remove(Direction.RIGHT)

    def moveUp(self):
        self.maze[self.ly, self.lx] = 0.5
        self.ly = self.ly - 1
        self.fitness = 0

    def moveDown(self):
        self.maze[self.ly, self.lx] = 0.5
        self.ly = self.ly + 1
        self.fitness = 0

    def moveRight(self):
        self.maze[self.ly, self.lx] = 0.5
        self.lx = self.lx + 1
        self.fitness = 0

    def moveLeft(self):
        self.maze[self.ly, self.lx] = 0.5
        self.lx = self.lx - 1
        self.fitness = 0

    def tele(self, x, y):
        self.lx = x
        self.ly = y
