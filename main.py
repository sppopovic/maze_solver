from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_clr):
        line.draw(self.canvas, fill_clr)

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point_1 = point1
        self.point_2 = point2
    
    def draw(self, canvas, fill_clr):
        canvas.create_line(self.point_1.x, self.point_1.y,
            self.point_2.x, self.point_2.y, fill=fill_clr, width = 2)

if __name__ == "__main__":
    win = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(200, 200)
    p3 = Point(400,100)
    p4 = Point(100,500)
    l1 = Line(p1, p2)
    l2 = Line(p3, p4)
    l3 = Line(p2, p4)
    l4 = Line(p1, p3)
    l1.draw(win.canvas, "red")
    l2.draw(win.canvas, "blue")
    l3. draw(win.canvas, "green")
    l4.draw(win.canvas, "pink")
    win.wait_for_close()

# main()
