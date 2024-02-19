from graphics import Window
from Maze import maze


def main():
    num_rows = 10
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    da_maze = maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    da_maze.build_maze()
    da_maze.solve()
    win.wait_for_close()


main()