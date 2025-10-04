clicked_rows = -1 # unclicked rows 
clicked_cols = -1 # unclicked cols
cell_size = 67 # size of cell
table = [] # table for numbers

def load_sudoku(filename): # load numbers from text file
    global table
    nums = loadStrings(filename) # nums for load numbers form text file
    for num in nums:
        rows = [] # rows for rows in nums
        for n in num: # n for each column in num
            rows.append(int(n)) # add int n to rows
        table.append(rows) # add rows to table

def draw_num(): # draw numbers from table
    global table
    for i in range(9):
        for j in range(9):
            if table[i][j] != 0: # check if table is not empty
                text(table[i][j],cell_size * j + cell_size / 2,cell_size * i + cell_size / 2) # write number

def draw_table(): # draw sudoku table
    for i in range(8): # draw 8 vertical lines
        strokeWeight(1)
        if i == 2 or i== 5: 
            strokeWeight(2)
        line(cell_size+cell_size*i,0,cell_size+cell_size*i,height) # draw each line
        
    for i in range(8): # draw 8 horizontal lines
        strokeWeight(1)
        if i == 2 or i== 5:
            strokeWeight(2)
        line(0,cell_size+cell_size*i,width,cell_size+cell_size*i) # draw each line

def mousePressed(): # mouse function for clicked
    global clicked_rows,clicked_cols
    rows = floor(mouseY/ cell_size) # rows for mouseY in cell_size
    cols = floor(mouseX / cell_size) # cols for mouseX in cell_size
    if (rows >= 0 and rows < 9) and (cols >= 0 and cols < 9): # 9 x 9 table
        clicked_rows = rows # clicked rows = rows
        clicked_cols = cols # clicked cols = cols
        
def keyPressed(): # input number
    if clicked_rows != -1 and clicked_cols != -1: # check if cell_size is unclicked
        if table[clicked_rows][clicked_cols] == 0: # if number in table == 0 or empty
            if key >= '1' and key <= '9': # if keyboard between 1 to 9
                table[clicked_rows][clicked_cols] = int(key) # number in table = int(ket)
        
def setup():
    size(600,600) 
    load_sudoku("sudoku.txt") # load sudoku numbers
    textAlign(CENTER,CENTER) # set text to center
    textSize(20) # size of text
    
def draw():
    background(200)
    draw_table() # draw sudoku table
    draw_num()  # draw numbers from table
    for i in range(9): # loop for mousePressed funtion
        for j in range(9):
            x = j * cell_size
            y = i * cell_size
            if i == clicked_rows and j == clicked_cols:  # if cell is clicked
                fill(0, 200, 0) # fill green
                rect(x, y, cell_size, cell_size) # draw green rectangle in clicked cell
            else: # if not
                fill(0) # fill black 
                

            
            
            
            
