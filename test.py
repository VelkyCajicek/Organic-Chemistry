import turtle
import tkinter as tk

class DraggableLines:
    def __init__(self, canvas):
        self.canvas = canvas
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        
        self.lines = []
        self.selected_line = None
        self.dragging = False
        self.start_x = 0
        self.start_y = 0

        self.create_initial_lines()

        self.canvas.bind("<Button-1>", self.select_line)
        self.canvas.bind("<B1-Motion>", self.drag_line)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)

    def create_initial_lines(self):
        # Create some initial lines for the user to drag
        self.add_line(-100, 100, 100, 100)
        self.add_line(-100, -100, 100, -100)
        self.add_line(-200, 0, 200, 0)

    def add_line(self, x1, y1, x2, y2):
        line = turtle.RawTurtle(self.screen)
        line.penup()
        line.goto(x1, y1)
        line.pendown()
        line.goto(x2, y2)
        self.lines.append({'turtle': line, 'start': (x1, y1), 'end': (x2, y2)})
        self.screen.update()

    def select_line(self, event):
        x, y = event.x - self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2 - event.y
        for line in self.lines:
            if self.point_near_line(x, y, line['start'], line['end']):
                self.selected_line = line
                self.start_x = x
                self.start_y = y
                self.dragging = True
                break

    def drag_line(self, event):
        if self.selected_line and self.dragging:
            x, y = event.x - self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2 - event.y
            dx = x - self.start_x
            dy = y - self.start_y
            new_start = (self.selected_line['start'][0] + dx, self.selected_line['start'][1] + dy)
            new_end = (self.selected_line['end'][0] + dx, self.selected_line['end'][1] + dy)
            self.selected_line['turtle'].clear()
            self.selected_line['turtle'].penup()
            self.selected_line['turtle'].goto(new_start)
            self.selected_line['turtle'].pendown()
            self.selected_line['turtle'].goto(new_end)
            self.selected_line['start'] = new_start
            self.selected_line['end'] = new_end
            self.start_x = x
            self.start_y = y
            self.screen.update()

    def stop_drag(self, event):
        self.dragging = False
        self.selected_line = None

    def point_near_line(self, px, py, start, end):
        """Check if the point (px, py) is near the line segment from start to end"""
        threshold = 10  # pixels
        x1, y1 = start
        x2, y2 = end
        line_len = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        distance = abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1) / line_len
        return distance < threshold

def main():
    root = tk.Tk()
    root.title("Drag and Drop Lines with Turtle in Tkinter")
    
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    app = DraggableLines(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
