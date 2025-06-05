import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

def create_grid(canvas):
    cells = []

    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        row_cells = []
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            cell = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="grey", outline="black")
            row_cells.append(cell)
        cells.append(row_cells)  # Moved outside the inner loop

    return cells

def erase(event):
    x, y = event.x, event.y
    row = y // CELL_SIZE
    col = x // CELL_SIZE

    if 0 <= len(grid) and 0 <= col < len(grid[0]):
        canvas.itemconfig(grid[row][col], fill="white")



def main():
    global canvas, grid
    root = tk.Tk()
    root.title("Grid")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.bind("<B1-Motion>" , erase)
    canvas.pack()

    grid = create_grid(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
