clicked_rows = -1 # empty rows 
clicked_cols = -1 # empty cols
cell_size = 67 # size of cell
table = [] # table for numbers

def load_sudoku(filename):
    global table
    nums = loadStrings(filename)
    for num in nums:
        rows = []
        for n in num:
            rows.append(n)
        table.append(rows)

def draw_table():
    for i in range(8):
        strokeWeight(1)
        if i == 2 or i== 5:
            strokeWeight(2)
        line(cell_size+cell_size*i,0,cell_size+cell_size*i,height)
        
    for i in range(8):
        strokeWeight(1)
        if i == 2 or i== 5:
            strokeWeight(2)
        line(0,cell_size+cell_size*i,width,cell_size+cell_size*i)

def mousePressed():
    global clicked_rows,clicked_cols
    rows = floor(mouseY/ cell_size)
    cols = floor(mouseX / cell_size)
    if (rows >= 0 and rows < 9) and (cols >= 0 and cols < 9):
        clicked_rows = rows
        clicked_cols = cols
        
def setup():
    size(600,600)
    load_sudoku("sudoku.txt")
    
def draw():
    background(200)
    draw_table()
    for i in range(9):
        for j in range(9):
            x = j * cell_size
            y = i * cell_size
            if i == clicked_rows and j == clicked_cols:  
                fill(0, 200, 0)
                rect(x, y, cell_size, cell_size)
            else:
                fill(0)
    
            
