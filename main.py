from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
    
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas( self.__root , width= width, height= height)
        self.canvas.pack()
        self.runing = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.runing = True
        while self.runing == True:
            self.redraw()
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.runing = False

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class line:
    def __init__(self, point1, point2):
        self.x_1 = point1.getX()
        self.x_2 = point2.getX()
        self.y_1 = point1.getY()
        self.y_2 = point2.getY()
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.x_a, self.y_a,self.x_b,self.y_b, fill=fill_color, width=2
        )
class cell:
    def __init__(self, point1, point2):
        self.x_1 = point1.getX()
        self.x_2 = point2.getX()
        self.y_1 = point1.getY()
        self.y_2 = point2.getY()

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._win = False
    def draw(self,point_top_left,point_bottom_right):
def main():
    win = Window(800,600)
    pointA = point(200,200)
    pointB = point(600,400)
    lin = line(pointA,pointB)
    fill_color = "red"
    win.draw_line(lin, fill_color)
    win.wait_for_close()

main()