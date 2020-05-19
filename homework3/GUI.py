import pygame
from pygame.locals import *


class GUI(UI):

    def __init__(self, life, cell_size=10, speed=10):
        super().__init__(life)
        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = (self.width, self.height)
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)
        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))

    def draw_grid(self):
      for i in range(self.life.rows):
          for j in range(self.life.cols):
              size = self.cell_size
              rect = (j*size, i*size, size, size)
              if self.life.curr_generation[i][j] == 1:
                  pygame.draw.rect(self.screen, pygame.Color('green'), rect)
              else:
                  pygame.draw.rect(self.screen, pygame.Color('white'), rect)

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        # timedelay = pygame.time.wait(0)
        running = True
        paused = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                  running = False
                if event.type == pygame.KEYDOWN and event.key == K_p:
                  paused = not paused # flip the flag each time key pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #получить позицию курсора
                    xcoord, ycoord = event.pos
                    i, j = ycoord//self.cell_size, xcoord//self.cell_size 
                    self.life.curr_generation[i][j] = 1
            self.draw_grid()          
            self.draw_lines()
            pygame.display.flip()
            if not paused:
              self.life.step()                    
              clock.tick(self.speed)
              if not (self.life.is_max_generations_exceeded and self.life.is_changing):
                running = False
        pygame.quit()
