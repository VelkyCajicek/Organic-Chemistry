import tkinter as tk
from tkinter.colorchooser import askcolor

class DraggableShapes:
    def __init__(self, canvas):
        self.canvas = canvas
        self.shapes = {}
        self.selected_shape = None
        self.dragging = False
        self.start_x = 0
        self.start_y = 0

        self.create_menu()

        self.canvas.bind("<Button-1>", self.select_shape)
        self.canvas.bind("<B1-Motion>", self.drag_shape)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)

    def create_menu(self):
        self.menu_frame = tk.Frame(self.canvas, bg='white')
        self.menu_frame.place(x=0, y=0)

        rect_button = tk.Button(self.menu_frame, text="Add Rectangle", command=self.add_rectangle)
        rect_button.pack(side=tk.TOP, padx=5, pady=5)

        oval_button = tk.Button(self.menu_frame, text="Add Oval", command=self.add_oval)
        oval_button.pack(side=tk.TOP, padx=5, pady=5)

        color_button = tk.Button(self.menu_frame, text="Change Outline Color", command=self.change_outline_color)
        color_button.pack(side=tk.TOP, padx=5, pady=5)

        width_button = tk.Button(self.menu_frame, text="Change Outline Width", command=self.change_outline_width)
        width_button.pack(side=tk.TOP, padx=5, pady=5)

    def add_rectangle(self):
        rect = self.canvas.create_rectangle(50, 50, 150, 150, fill="red", outline="black", width=2)
        self.shapes[rect] = {'type': 'rectangle', 'start': (50, 50), 'end': (150, 150)}

    def add_oval(self):
        oval = self.canvas.create_oval(200, 50, 300, 150, fill="blue", outline="black", width=2)
        self.shapes[oval] = {'type': 'oval', 'start': (200, 50), 'end': (300, 150)}

    def select_shape(self, event):
        x, y = event.x, event.y
        shape = self.canvas.find_closest(x, y)
        if shape:
            shape_id = shape[0]
            if shape_id in self.shapes:
                self.selected_shape = shape_id
                self.start_x = x
                self.start_y = y
                self.dragging = True

    def drag_shape(self, event):
        if self.selected_shape and self.dragging:
            x, y = event.x, event.y
            dx = x - self.start_x
            dy = y - self.start_y
            self.canvas.move(self.selected_shape, dx, dy)
            self.shapes[self.selected_shape]['start'] = (
                self.shapes[self.selected_shape]['start'][0] + dx,
                self.shapes[self.selected_shape]['start'][1] + dy
            )
            self.shapes[self.selected_shape]['end'] = (
                self.shapes[self.selected_shape]['end'][0] + dx,
                self.shapes[self.selected_shape]['end'][1] + dy
            )
            self.start_x = x
            self.start_y = y

    def stop_drag(self, event):
        self.dragging = False
        self.selected_shape = None

    def change_outline_color(self):
        if self.selected_shape:
            color = askcolor()[1]  # This opens a color chooser and returns the selected color
            if color:
                self.canvas.itemconfig(self.selected_shape, outline=color)

    def change_outline_width(self):
        if self.selected_shape:
            new_width = tk.simpledialog.askinteger("Input", "Enter new outline width:", minvalue=1, maxvalue=10)
            if new_width is not None:
                self.canvas.itemconfig(self.selected_shape, width=new_width)

def main():
    root = tk.Tk()
    root.title("Drag and Drop Shapes in Tkinter")
    
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    app = DraggableShapes(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
