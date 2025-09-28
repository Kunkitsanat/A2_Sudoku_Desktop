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
            rows.append(int(n))
        table.append(rows)

def draw_num():
    global table
    for i in range(9):
        for j in range(9):
            if table[i][j] != 0:
                text(table[i][j],cell_size * j + cell_size / 2,cell_size * i + cell_size / 2)

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
        
def keyPressed():
    if clicked_rows != -1 and clicked_cols != -1:
        if table[clicked_rows][clicked_cols] == 0:
            if key >= '1' and key <= '9':
                table[clicked_rows][clicked_cols] = int(key)
        
def setup():
    size(600,600)
    load_sudoku("sudoku.txt")
    textAlign(CENTER,CENTER)
    textSize(20)
    
def draw():
    background(200)
    draw_table()
    draw_num()
    for i in range(9):
        for j in range(9):
            x = j * cell_size
            y = i * cell_size
            if i == clicked_rows and j == clicked_cols:  
                fill(0, 200, 0)
                rect(x, y, cell_size, cell_size)
            else:
                fill(0)
                

            
            
            
            
