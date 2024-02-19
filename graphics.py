from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
    
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas( self.__root,background="white" , width= width, height= height)
        self.canvas.pack()
        self.runing = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.runing = True
        while self.runing:
            self.redraw()
        print("window closed...")
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.runing = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 =point2
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y,self.p2.x,self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)