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

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point_1 = point1
        self.point_2 = point2
    
    def draw(self, canvas, fill_clr):
        canvas.create_line

if __name__ == "__main__":
    win = Window(800, 600)
    win.wait_for_close()

# main()
