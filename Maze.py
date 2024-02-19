import random
from graphics import Point, Window
from Cell import cell
from time import sleep

class maze:
    def __init__(self, x1, y1, num_rows= 0, num_cols = 0, cell_size_x = 1, cell_size_y = 1, win=None,seed=None):
        self.x_1 = x1
        self.y_1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x1 = cell_size_x
        self.cell_size_y1 = cell_size_y
        self._win = win
        self._cells = []
        self._cell_registry = []
        self._create_cells()
        if seed != None:
            random.seed(seed)
    
    def _create_cells(self):
        
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                self._cell_registry.append(cell(self._win))
                col_cells.append(self._cell_registry[-1])
            self._cells.append(col_cells)
            
        for I in range(self.num_cols):
            for J in range(self.num_rows):
                self._draw_cell(I, J)
                
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x_1 + i * self.cell_size_x1
        y1 = self.y_1 + j * self.cell_size_y1
        x2 = x1 + self.cell_size_x1
        y2 = y1 + self.cell_size_y1
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()
    def _animate(self):
        if self._win != None:
            return
        self._win.redraw()
        sleep(0.1)
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        exit_cell = self._cells[self.num_cols -1 ][self.num_rows -1]
        exit_cell.has_bottom_wall = False
        exit_cell.is_end = True
        if self._win is None:
            return
        self._win.canvas.create_line(
            entrance.x_1, entrance.y_1,entrance.x_2,entrance.y_1, fill= "white", width=2)
        self._win.canvas.create_line(
            exit_cell.x_1, exit_cell.y_2,exit_cell.x_2,exit_cell.y_2, fill= "white", width=2)
        
    def _break_walls_r(self,i,j):
        self._win.redraw()
        sleep(.1)
        _i = i
        _j = j
        cur_cell = self._cells[i][j]
        x1 = cur_cell.x_1
        x2 = cur_cell.x_2
        y1 = cur_cell.y_1
        y2 = cur_cell.y_2
        
        
        cur_cell.visited = True
        while True:
            next_i = _i
            next_j = _j
            to_visit = []
            #check if north cell exist
            if j != 0:
                #check north cell
                if self._cells[i][j-1].visited == False:
                    to_visit.append("north")
            #check if south cell exist
            if j < self.num_rows -1:
                #check south cell
                if self._cells[i][j+1].visited == False:
                    to_visit.append("south")
            #check if east cell exist
            if i < self.num_cols -1:
                #check east cell
                if self._cells[i+1][j].visited == False:
                    to_visit.append("east")
            #check if west cell exist
            if i != 0 :
                if self._cells[i-1][j].visited == False:
                    to_visit.append("west")
            if len(to_visit) == 0:
                cur_cell.draw(x1,y1,x2,y2)
                
                return
            next_dric = random.choice(to_visit)
            next_cell = None
            if next_dric== "north":
                next_cell = self._cells[i][j-1]
                cur_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
                next_j -= 1
                
                
                
            elif next_dric == "south":
                next_cell = self._cells[i][j+1]
                cur_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
                next_j += 1
                
                
            elif next_dric == "east":
                next_cell = self._cells[i+1][j]
                cur_cell.has_right_wall = False
                next_cell.has_left_wall = False
                next_i += 1
                
                
            elif next_dric == "west":
                next_cell = self._cells[i-1][j]
                cur_cell.has_left_wall = False
                next_cell.has_right_wall = False
                next_i -= 1
                
            else:
                print("dric error")
            cur_cell.draw(x1,y1,x2,y2)   
            
            self._break_walls_r(next_i,next_j)
    
    def _reset_cells_visited(self):
        for cell in self._cell_registry:
            cell.visited = False
            cell.draw(cell.x_1,cell.y_1,cell.x_2,cell.y_2)
    def build_maze(self):
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    def solve(self):
        return self._solve_r()
    def _solve_r(self,i=0,j=0):
        cur_cell = self._cells[i][j]

        x1 = cur_cell.x_1
        x2 = cur_cell.x_2
        y1 = cur_cell.y_1
        y2 = cur_cell.y_2
        _i = i
        _j = j

        self._animate()
        cur_cell.visited = True
        if cur_cell.is_end == True:
            return True
        
        to_visit = []
        #check if north cell exist
        if j != 0:
            #check north cell
            if self._cells[i][j-1].visited == False and cur_cell.has_top_wall == False:
                to_visit.append("north")
                
        #check if south cell exist
        if j < self.num_rows -1:
            #check south cell
             if self._cells[i][j+1].visited == False and cur_cell.has_bottom_wall == False:
                to_visit.append("south")
                
        #check if east cell exist
        if i < self.num_cols -1:
            #check east cell
            if self._cells[i+1][j].visited == False and cur_cell.has_right_wall == False:
                to_visit.append("east")
                
        #check if west cell exist
        if i != 0 :
            if self._cells[i-1][j].visited == False and cur_cell.has_left_wall == False:
                to_visit.append("west")
                
        #if len(to_visit) == 0:
                #cur_cell.draw(x1,y1,x2,y2)
                
        for direction in to_visit:
            next_i = _i
            next_j = _j
            if direction == "north":
                next_cell = self._cells[i][j-1]
                cur_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
                next_j -= 1
                
                
                
            elif direction == "south":
                next_cell = self._cells[i][j+1]
                cur_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
                next_j += 1
                
                
            elif direction == "east":
                next_cell = self._cells[i+1][j]
                cur_cell.has_right_wall = False
                next_cell.has_left_wall = False
                next_i += 1
                
                
            elif direction == "west":
                next_cell = self._cells[i-1][j]
                cur_cell.has_left_wall = False
                next_cell.has_right_wall = False
                next_i -= 1
                
            else:
                print("dric error")
            
            to_cell = self._cells[next_i][next_j]
            cur_cell.draw_move(to_cell)
            if self._solve_r(next_i,next_j):
                return True
            cur_cell.draw_move( to_cell, True)
        
        return False
        #if current cell is an end cell OR leads to the end cell
            #return true
        #esle
            #reurn false