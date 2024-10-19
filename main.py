import pygame

pygame.init()

screen_width = 300
screen_height = 300
pos = []
current_player = 1
winner = 0
game_over = False
line_width = 6
game_state = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
font = pygame.font.SysFont(None, 40)
again_rect = pygame.Rect(screen_width//2 - 80, screen_height//2 + 53, 160, 50)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')
pygame.display.update()
pygame.quit()