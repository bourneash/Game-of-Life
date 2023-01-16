import os
import time
import yaml

class GameOfLife:
    def __init__(self, seed_file):
        with open(seed_file, 'r') as f:
            seed = yaml.safe_load(f)
            self.grid = seed['grid']
            self.grid_height = len(self.grid)
            self.grid_width = len(self.grid[0])
            self.refresh_rate = seed['refresh_rate']

    def print_grid(self):
        os.system('clear')
        for row in self.grid:
            print(' '.join(row))

    def run(self):
        while True:
            self.print_grid()
            self.update_grid()
            time.sleep(self.refresh_rate)

    def update_grid(self):
        new_grid = [['.' for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                live_neighbors = self.count_live_neighbors(i, j)
                if self.grid[i][j] == 'X':
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[i][j] = '.'
                    else:
                        new_grid[i][j] = 'X'
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = 'X'
        self.grid = new_grid

    def count_live_neighbors(self, i, j):
        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if i+x < 0 or i+x >= self.grid_height or j+y < 0 or j+y >= self.grid_width:
                    continue
                if self.grid[i+x][j+y] == 'X':
                    count += 1
        return count


if __name__ == '__main__':
    game = GameOfLife('seed.yaml')
    game.run()
