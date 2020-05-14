import random

import pygame
from pygame.locals import *

class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        
        # стартовое поле
        self.grid = self.create_grid(randomize=True)
        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))

    def create_grid(self, randomize=False):
      grid = [[0]*self.cell_width for i in range(self.cell_height)]
      if randomize:
        for i in range(self.cell_height):
          for j in range(self.cell_width):
            grid[i][j] = random.randint(0,1)
      return grid

    def draw_grid(self):
      for i in range(self.cell_height):
          for j in range(self.cell_width):
              size = self.cell_size
              rect = (j*size, i*size, size, size)
              if self.grid[i][j] == 1:
                  pygame.draw.rect(self.screen, pygame.Color('green'), rect)
              else:
                  pygame.draw.rect(self.screen, pygame.Color('white'), rect)
    
    def get_neighbours(self, cell):
      i, j = cell
      right_wrap = (j + 1)%self.cell_width
      bot_wrap = (i + 1)%self.cell_height
      return [(i-1, j-1), (i-1, j), (i-1, right_wrap),
          (i, j-1), (i, right_wrap),
          (bot_wrap, j-1), (bot_wrap, j), (bot_wrap, right_wrap)]

    def get_next_generation(self):
        cells_to_update = []
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                neighbours = self.get_neighbours((i,j))
                s = sum(self.grid[n[0]][n[1]] for n in neighbours)
                if self.grid[i][j] == 0 and s == 3:
                  cells_to_update.append((i, j, 1))
                elif self.grid[i][j] == 1 and (s < 2 or s > 3):
                  cells_to_update.append((i, j, 0))
        for c in cells_to_update:
            self.grid[c[0]][c[1]] = c[2]
        return self.grid        

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.get_next_generation()
            self.draw_grid()          
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


