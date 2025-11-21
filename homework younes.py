import random
import time
import os
# possible steps for movement (x or y changes)
possibilities = [-1, 0, 1]
# class : point 
class Point:
    # move the point inside boundaries
    def move(self, dx=0, dy=0, W=-1, H=-1):
        new_x = self.get_x() + dx
        new_y = self.get_y() + dy
        # if no boundaries are given free movement
        if W == -1 and H == -1:
            self.set_x(new_x)
            self.set_y(new_y)
            return
        # Apply boundaries
        if new_x >= W:
            new_x = W - 1
        if new_x < 0:
            new_x = 0

        if new_y >= H:
            new_y = H - 1
        if new_y < 0:
            new_y = 0

        self.set_x(new_x)
        self.set_y(new_y)
    # Random movement by one step in any direction 
    def move_random_step(self, W, H):
        dx = random.choice(possibilities)
        dy = random.choice(possibilities)
        self.move(dx, dy, W, H)

    def display(self):
        print(f"The coordinates of the Point are ({self.get_x()}, {self.get_y()})")
    # Poper constructor
    def __init__(self, x, y, marker="*"):
        self.__x = x
        self.__y = y
        self.marker = marker
    # Getters and setters 
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value
    # Class : Grid
class Grid:
    def __init__(self, W, H, points=[]):
        self.W = W
        self.H = H
        self.points = points    # List of point objects

    def add_point(self, point):
        self.points.append(point)
    # Drawing the grid with its poits 
    def display(self):
        print(" " + "#" * self.W)
        for y in range(self.H):
            print("#", end="")
            for x in range(self.W):
                marker = " "
                for p in self.points:
                    if (p.get_x() == x) and (p.get_y() == y):
                        marker = p.marker
                        break
                print(marker, end="")
            print("#")
        print(" " + "#" * self.W)
# Main program 
p1 = Point(3, 3, "*")
p2 = Point(7, 7, "*")

grid = Grid(10, 10)

grid.add_point(p1)
grid.add_point(p2)

while True:
    p1.move_random_step(grid.W, grid.H)
    p2.move_random_step(grid.W, grid.H)
    grid.display()
    time.sleep(0.05)
    os.system('cls')
