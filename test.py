import tkinter as tk

class DragDropShapes:
    def __init__(self, root):
        self.root = root
        self.root.title("Drag and Drop Shapes")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Create shapes
        self.create_shapes()

        # Bind events for dragging
        self.canvas.tag_bind("shape", "<ButtonPress-1>", self.on_start)
        self.canvas.tag_bind("shape", "<B1-Motion>", self.on_drag)

        self.drag_data = {"x": 0, "y": 0, "item": None}

    def create_shapes(self):
        self.canvas.create_rectangle(50, 50, 150, 150, fill="blue", tags="shape")
        self.canvas.create_oval(200, 50, 300, 150, fill="red", tags="shape")
        self.canvas.create_polygon(350, 50, 400, 150, 450, 50, fill="green", tags="shape")

    def on_start(self, event):
        # Record the item and its location
        self.drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag(self, event):
        # Compute how much the mouse has moved
        delta_x = event.x - self.drag_data["x"]
        delta_y = event.y - self.drag_data["y"]

        # Move the object the appropriate amount
        self.canvas.move(self.drag_data["item"], delta_x, delta_y)

        # Record the new position
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

if __name__ == "__main__":
    root = tk.Tk()
    app = DragDropShapes(root)
    root.mainloop()
