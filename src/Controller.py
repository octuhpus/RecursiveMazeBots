import random

import cv2
import time
import Enums as ens

from MazeBot import MazeBot

NUM_BOTS = 5


class Controller:
    def __init__(self, maze, width, height):
        self.maze = maze
        self.width = width
        self.height = height
        self.isDone = False
        self.deadSet = []
        self.unexplored = []

        cv2.namedWindow('Maze', cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Maze", 500, 500)

        goal = False

        while not goal:
            self.randx = random.randint(2, self.height - 2)
            self.randy = random.randint(2, self.width - 2)
            if self.maze[self.randy, self.randx] == 0:
                continue
            else:
                self.maze[self.randy, self.randx] = .2
                goal = True

        bots = [MazeBot(maze, 2, 2) for _ in range(NUM_BOTS)]

        while not self.isDone:

            # self.maze[0, 2] = .5

            for bot in bots:
                bot.determineFitness(self.maze)

                if self.maze[bot.ly, bot.lx] == .2:
                    self.maze[bot.ly, bot.lx] == 0
                    self.isDone
                    print("Done!")
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    return

                if bot.fitness == 0 and bot not in self.deadSet:
                    self.deadSet.append(bot)

                if bot.fitness > 1:
                    self.unexplored.append(bot.lx)  # unexplored[0]
                    self.unexplored.append(bot.ly)  # unexplored[1]

                if bot in self.deadSet and bot.fitness > 0:
                    self.deadSet.remove(bot)
                # print(bot.fitness)

                if len(bot.openDir) > 0:
                    if bot.ly < self.randy and ens.Direction.DOWN in bot.openDir:
                        bot.moveDown()
                        print("D")
                    elif bot.ly > self.randy and ens.Direction.UP in bot.openDir:
                        bot.moveUp()
                        print("U")
                    elif bot.lx < self.randx and ens.Direction.RIGHT in bot.openDir:
                        bot.moveRight()
                        print("R")
                    elif bot.lx > self.randx and ens.Direction.LEFT in bot.openDir:
                        bot.moveLeft()
                        print("L")
                    else:
                        moveBot(random.choice(list(bot.openDir)), bot)
                        # print("R")
                elif len(bot.openDir) == 0 and len(self.unexplored) > 0:
                    self.maze[bot.ly, bot.lx] = .5
                    bot.tele(self.unexplored[0], self.unexplored[1])
                    self.deadSet.remove(bot)
                    self.unexplored.remove(self.unexplored[0])
                    self.unexplored.remove(self.unexplored[0])
                    if bot.fitness > 1:
                        print("HERE")
                        self.unexplored.append(bot.lx)  # unexplored[0]
                        self.unexplored.append(bot.ly)  # unexplored[1]
                else:
                    self.maze[bot.ly, bot.lx] = .5

            self.isDoneCheck()
            self.displayImage()

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def isDoneCheck(self):

        if len(self.deadSet) == NUM_BOTS:
            self.isDone = True
            print("Done!")
        else:
            self.isDone = False

    def displayImage(self):
        cv2.imshow('Maze', self.maze)
        cv2.waitKey(1)
        time.sleep(0.0)


def reorder_bots(bots):
    bots.sort(key=lambda bot: bot.fitness, reverse=True)


def moveBot(direction, bot):
    if direction == ens.Direction.UP:
        bot.moveUp()
    elif direction == ens.Direction.DOWN:
        bot.moveDown()
    elif direction == ens.Direction.LEFT:
        bot.moveLeft()
    elif direction == ens.Direction.RIGHT:
        bot.moveRight()
