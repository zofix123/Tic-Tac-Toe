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

def draw_grid():
    line_width = 6
    bg = (255, 200, 255)
    grid = (0, 0, 0)
    screen.fill(bg)
    for i in range(1, 3):
        pygame.draw.line(screen, grid, (0, i*(screen_height//3)), (screen_width, i*(screen_height//3)), line_width)
        pygame.draw.line(screen, grid, (i*(screen_width//3), 0), (i*(screen_width//3), screen_height), line_width)

def draw_markers():
    x_pos = 0
    for x in game_state:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, (0, 255, 0), (x_pos*screen_width//3 + 15, y_pos*screen_height//3 + 15), (x_pos*screen_width//3 + 85, y_pos*screen_height//3 + 85), line_width)
                pygame.draw.line(screen, (0, 255, 0), (x_pos*screen_width//3 + 15, y_pos*screen_height//3 + 85), (x_pos*screen_width//3 + 85, y_pos*screen_height//3 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, (255, 0, 0), (x_pos*screen_width//3 + 50, y_pos*screen_height//3 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

run = True
while run:

    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            if game_state[mouse_x // (screen_width // 3)][mouse_y // (screen_height // 3)] == 0:
                game_state[mouse_x // (screen_width // 3)][mouse_y // (screen_height // 3)] = current_player
                current_player *= -1
    pygame.display.update()
pygame.quit()