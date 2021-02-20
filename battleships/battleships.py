import sys
import pygame
from pygame.locals import KEYDOWN, K_q
import gameboard

# CONSTANTS:
screensize = width, height = 1400, 780
board_prop = {'surface': False, 'gridWH': 496, 'gridOrigin': (90, 160), 'gridCells': 8, 'lineWidth': 2,
              'gridOrigin_P2': (820, 160)}
board_surface = pygame.display.set_mode(screensize)

# Colour palette
ocean = (0, 105, 148)

# Images
Header = pygame.image.load('../data/images/Label.png')
side_label = pygame.image.load('../data/images/side_label.png')
Player1 = pygame.image.load('../data/images/Player1.png')
Player2 = pygame.image.load('../data/images/Player2.png')
ship_sunk = pygame.image.load('../data/images/ship_sunk.png')
your_turn = pygame.image.load('../data/images/your_turn.png')
press_q = pygame.image.load('../data/images/Press_Q.png')


# Main function
def main():
    pygame.init()
    cell_border = 7
    cell_inc = 62
    player1 = True
    p1_hits_list = []
    p2_hits_list = []
    p1_misses_list = []
    p2_misses_list = []
    p1_ships_list = [(0, 0), (1, 0), (2, 0)]
    p2_ships_list = [(0, 2), (0, 3), (0, 4)]

    board = gameboard.Board(board_prop, board_surface)
    board_surface.fill(ocean)
    board_surface.blit(Player1, (10, 10))
    board_surface.blit(Header, (100, 100))
    board_surface.blit(side_label, (40, 160))
    board_surface.blit(your_turn, (180, 50))
    board.draw_square_grid(board_prop['gridOrigin'])
    board_surface.blit(Player2, (720, 10))
    board_surface.blit(Header, (830, 100))
    board_surface.blit(side_label, (770, 160))
    board.draw_square_grid(board_prop['gridOrigin_P2'])
    board.place_cells(board_prop['gridOrigin'])
    board.place_cells(board_prop['gridOrigin_P2'])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_q:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if player1:
                    start_pos_x = board_prop['gridOrigin_P2'][0]
                    start_pos_y = board_prop['gridOrigin_P2'][1]
                    x = ((x - (board_prop['gridOrigin_P2'][0])) // cell_inc)
                    y = ((y - (board_prop['gridOrigin_P2'][1])) // cell_inc)
                    if x in range(8) and y in range(8):
                        ship = p2_ships_list
                        pos = (x, y)
                        if pos in ship:
                            player1 = False
                            p2_hits_list.append(pos)
                            board_surface.blit(your_turn, (900, 50))
                            pygame.draw.rect(board_surface, ocean, (180, 50, 200, 50))
                            for shots in p2_hits_list:
                                if pos == shots:
                                    board.draw_hit(start_pos_x + cell_border + cell_inc * x,
                                                   start_pos_y + cell_border + cell_inc * y, 50, 50)
                                    p2_hits_list.sort()
                                    if p2_hits_list == p2_ships_list:
                                        board_surface.blit(ship_sunk, (950, 330))
                                        board_surface.blit(press_q, (180, 50))
                        elif pos not in ship:
                            player1 = False
                            p1_misses_list.append(pos)
                            board_surface.blit(your_turn, (900, 50))
                            pygame.draw.rect(board_surface, ocean, (180, 50, 200, 50))
                            board.draw_miss(start_pos_x + cell_border + cell_inc * x,
                                            start_pos_y + cell_border + cell_inc * y, 50, 50)
                else:
                    start_pos_x = board_prop['gridOrigin'][0]
                    start_pos_y = board_prop['gridOrigin'][1]
                    x = ((x - (board_prop['gridOrigin'][0])) // cell_inc)
                    y = ((y - (board_prop['gridOrigin'][1])) // cell_inc)
                    if x in range(8) and y in range(8):
                        ship = p1_ships_list
                        pos = (x, y)
                        if pos in ship:
                            player1 = True
                            p1_hits_list.append(pos)
                            pygame.draw.rect(board_surface, ocean, (880, 50, 200, 50))
                            board_surface.blit(your_turn, (180, 50))
                            for shots in p1_hits_list:
                                if pos == shots:
                                    board.draw_hit(start_pos_x + cell_border + cell_inc * x,
                                                   start_pos_y + cell_border + cell_inc * y, 50, 50)
                                    p1_hits_list.sort()
                                    if p1_hits_list == p1_ships_list:
                                        board_surface.blit(ship_sunk, (250, 330))
                                        board_surface.blit(press_q, (180, 50))

                        elif pos not in ship:
                            player1 = True
                            p2_misses_list.append(pos)
                            pygame.draw.rect(board_surface, ocean, (880, 50, 200, 50))
                            board_surface.blit(your_turn, (180, 50))
                            board.draw_miss(start_pos_x + cell_border + cell_inc * x,
                                            start_pos_y + cell_border + cell_inc * y, 50, 50)
        pygame.display.update()


if __name__ == '__main__':
    main()
