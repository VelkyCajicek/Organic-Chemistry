import tkinter as tk

class DraggableShapes:
    def __init__(self, canvas : tk.Canvas):
        self.canvas = canvas
        self.shapes = {}
        self.selected_shape = None
        self.lastSelectedShape = None
        self.dragging = False
        self.start_x = 0
        self.start_y = 0

        self.create_menu()

        self.canvas.bind("<Button-1>", self.select_shape)
        self.canvas.bind("<B1-Motion>", self.drag_shape)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)
        self.canvas.bind("<Button-2>", self.removeShape())

    def create_menu(self):
        self.menu_frame = tk.Frame(self.canvas, bg='white')
        self.menu_frame.place(x=0, y=0)

        rect_button = tk.Button(self.menu_frame, text="Add Rectangle", command=self.add_rectangle)
        rect_button.pack(side=tk.TOP, padx=5, pady=5)

        oval_button = tk.Button(self.menu_frame, text="Add Oval", command=self.add_oval)
        oval_button.pack(side=tk.TOP, padx=5, pady=5)

    def add_rectangle(self):
        rect = self.canvas.create_rectangle(50, 50, 150, 150, fill="red", outline="blue", width=1)
        self.shapes[rect] = {'type': 'rectangle', 'start': (50, 50), 'end': (150, 150)}

    def add_oval(self):
        oval = self.canvas.create_oval(200, 50, 300, 150, fill="blue", outline="red", width=1)
        self.shapes[oval] = {'type': 'oval', 'start': (200, 50), 'end': (300, 150)}

    def removeShape(self):
        print(self.selected_shape)
        self.canvas.delete(self.lastSelectedShape)
        
    def select_shape(self, event):
        x, y = event.x, event.y
        shape = self.canvas.find_closest(x, y)
        if shape:
            shape_id = shape[0]
            if shape_id in self.shapes:
                self.selected_shape = shape_id
                if(self.lastSelectedShape != shape_id and self.lastSelectedShape != None): # Deselects the previous object
                    self.canvas.itemconfig(self.lastSelectedShape, outline="purple")
                self.canvas.itemconfig(shape_id, outline="green") # Changes shape outline to show which is selected
                self.lastSelectedShape = shape_id

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

def main():
    root = tk.Tk()
    root.title("Drag and Drop Shapes in Tkinter")
    
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    app = DraggableShapes(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()