from graphics import Line, Point

class cell:
    def __init__(self, win= None):
        self.x_1 = None
        self.x_2 = None
        self.y_1 = None
        self.y_2 = None

       
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self._win = win
        self.visited = False
        self.is_end = False

        
    def draw(self,x1,y1,x2,y2):
        #if self._win is None:
         #   return
        self.x_1 = x1
        self.x_2 = x2
        self.y_1 = y1
        self.y_2 = y2
        if self.visited == False:
            self.line_color = "black"
        else:
            self.line_color = "red"
        if self.has_left_wall == True:
            self._win.canvas.create_line(
            self.x_1, self.y_1,self.x_1,self.y_2, fill= self.line_color, width=2)
        else:
            self._win.canvas.create_line(
            self.x_1, self.y_1,self.x_1,self.y_2, fill= "white", width=2)
        if self.has_right_wall == True:
            self._win.canvas.create_line(
            self.x_2, self.y_1,self.x_2,self.y_2, fill= self.line_color, width=2)
        else:
            self._win.canvas.create_line(
            self.x_2, self.y_1,self.x_2,self.y_2, fill= "white", width=2)
        if self.has_top_wall == True:
            self._win.canvas.create_line(
            self.x_1, self.y_1,self.x_2,self.y_1, fill= self.line_color, width=2)
        else:
            self._win.canvas.create_line(
            self.x_1, self.y_1,self.x_2,self.y_1, fill= "white", width=2)
        if self.has_bottom_wall == True:
            self._win.canvas.create_line(
            self.x_1, self.y_2,self.x_2,self.y_2, fill= self.line_color, width=2)
        else:
            self._win.canvas.create_line(
            self.x_1, self.y_2,self.x_2,self.y_2, fill= "white", width=2)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_mid = (self.x_1 + self.x_2) / 2
        y_mid = (self.y_1 + self.y_2) / 2

        to_x_mid = (to_cell.x_1 + to_cell.x_2) / 2
        to_y_mid = (to_cell.y_1 + to_cell.y_2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self.x_1 > to_cell.x_1:
            line = Line(Point(self.x_1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell.x_2, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self.x_1 < to_cell.x_1:
            line = Line(Point(x_mid, y_mid), Point(self.x_2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell.x_1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self.y_1 > to_cell.y_1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self.y_1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell.y_2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self.y_1 < to_cell.y_1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self.y_2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell.y_1))
            self._win.draw_line(line, fill_color)
