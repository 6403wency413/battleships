import pygame

# Colour palette
border = (255, 255, 255)
ship = (157, 162, 155)
hit = (255, 0, 0)
miss = (255, 255, 255)


class Board:
    def __init__(self, board_param, screen_mode):
        self.gridWH = board_param['gridWH']
        self.gridCells = board_param['gridCells']
        self.surface = board_param['surface']
        self.gridOrigin = board_param['gridOrigin']
        self.gridOrigin_P2 = board_param['gridOrigin_P2']
        self.lineWidth = board_param['lineWidth']
        self.screen_mode = screen_mode

    def place_cells(self, grid_origin_p1=None, grid_origin_p2=None):
        # GET CELL DIMENSIONS...
        cell_border = 6
        cell_dim_x = cell_dim_y = (self.gridWH / self.gridCells) - (cell_border * 2)
        # DOUBLE LOOP
        for row in range(8):
            for column in range(8):
                if grid_origin_p1 is not None:
                    self.draw_square_cell(
                        grid_origin_p1[0] + (cell_dim_y * row)
                        + cell_border + (2 * row * cell_border) + self.lineWidth / 2,
                        grid_origin_p1[1] + (cell_dim_x * column)
                        + cell_border + (2 * column * cell_border) + self.lineWidth / 2, cell_dim_x, cell_dim_y)
                if grid_origin_p2 is not None:
                    self.draw_square_cell(
                        grid_origin_p2[0] + (cell_dim_y * row)
                        + cell_border + (2 * row * cell_border) + self.lineWidth / 2,
                        grid_origin_p2[1] + (cell_dim_x * column)
                        + cell_border + (2 * column * cell_border) + self.lineWidth / 2, cell_dim_x, cell_dim_y)

    # Draw filled rectangle at coordinates
    def draw_square_cell(self, x, y, dim_x, dim_y):
        pygame.draw.rect(
            self.screen_mode, ship,
            (x, y, dim_x, dim_y)
        )

    def draw_hit(self, x, y, dim_x, dim_y):
        pygame.draw.rect(
            self.screen_mode, hit,
            (x, y, dim_x, dim_y)
        )

    def draw_miss(self, x, y, dim_x, dim_y):
        pygame.draw.rect(
            self.screen_mode, miss,
            (x, y, dim_x, dim_y)
        )

    def draw_square_grid(self, origin):

        container_width_height = self.gridWH
        cont_x, cont_y = origin

        # DRAW Grid Border:
        # TOP lEFT TO RIGHT
        pygame.draw.line(
            self.screen_mode, border,
            (cont_x, cont_y),
            (container_width_height + cont_x, cont_y), self.lineWidth)
        # # BOTTOM lEFT TO RIGHT
        pygame.draw.line(
            self.screen_mode, border,
            (cont_x, container_width_height + cont_y),
            (container_width_height + cont_x,
             container_width_height + cont_y), self.lineWidth)
        # # LEFT TOP TO BOTTOM
        pygame.draw.line(
            self.screen_mode, border,
            (cont_x, cont_y),
            (cont_x, cont_y + container_width_height), self.lineWidth)
        # # RIGHT TOP TO BOTTOM
        pygame.draw.line(
            self.screen_mode, border,
            (container_width_height + cont_x, cont_y),
            (container_width_height + cont_x,
             container_width_height + cont_y), self.lineWidth)
        # # Center line
        pygame.draw.line(
            self.screen_mode, border,
            (700, 0),
            (700, 780), 5)

        # Get cell size, just one since its a square grid.
        cell_size = container_width_height / self.gridCells

        # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
        for x in range(self.gridCells):
            pygame.draw.line(
                self.screen_mode, border,
                (cont_x + (cell_size * x), cont_y),
                (cont_x + (cell_size * x), container_width_height + cont_y), 2)
            # # HORIZONTAL DIVISIONS
            pygame.draw.line(
                self.screen_mode, border,
                (cont_x, cont_y + (cell_size * x)),
                (cont_x + container_width_height, cont_y + (cell_size * x)), 2)
