import pathlib
import random

from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]

class GameOfLife:

    def __init__(self, size, randomize=True, max_generations=None):
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize=False):
      grid = [[0]*self.cols for i in range(self.rows)]
      if randomize:
        for i in range(self.rows):
          for j in range(self.cols):
            grid[i][j] = random.randint(0,1)
      return grid

    def get_neighbours(self, cell):
        i, j = cell
        right_wrap = (j + 1)%self.cols
        bot_wrap = (i + 1)%self.rows
        return [(i-1, j-1), (i-1, j), (i-1, right_wrap),
          (i, j-1), (i, right_wrap),
          (bot_wrap, j-1), (bot_wrap, j), (bot_wrap, right_wrap)]

    def get_next_generation(self):
        grid = self.curr_generation
        cells_to_update = []
        for i in range(self.rows):
            for j in range(self.cols):
                neighbours = self.get_neighbours((i,j))
                s = sum(self.grid[n[0]][n[1]] for n in neighbours)
                if grid[i][j] == 0 and s == 3:
                  cells_to_update.append((i, j, 1))
                elif grid[i][j] == 1 and (s < 2 or s > 3):
                  cells_to_update.append((i, j, 0))
        for c in cells_to_update:
            grid[c[0]][c[1]] = c[2]
        return grid

    def step(self):
        for i in self.rows:
          for j in range.cols:
            self.prev_generation[i][j] = self.curr_generation[i][j]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        return self.generations <= self.max_generations

    @property
    def is_changing(self) -> bool:
        return self.curr_generation == self.prev_generation
        

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        with open(filename) as f:
          data = f.read()
          return [[int(c) for c in i] for i in data.split()]

    def save(filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, 'w') as f:
          f.write("\n".join("".join(row) for row in self.curr_generation))


