import cell


class Grid:

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.grid = []

    def fill_grid(self):
        for y in range(self.y_size):
            x_list = []
            for x in range(self.x_size):
                new_cell = cell.Cell()
                x_list.append(new_cell)
            self.grid.append(x_list)

    def print_grid(self):
        for x_list in self.grid:
            print([elem.get_short_status() for elem in x_list])
