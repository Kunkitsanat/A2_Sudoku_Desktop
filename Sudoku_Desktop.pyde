s = 600
width = s
height = s

clicked_rows = -1 # unclicked rows 
clicked_cols = -1 # unclicked cols
cell_size = s / 9 # size of cell
table = [] # table for numbers
truth_value = [[1,1,1,1,1,1,1,1,1], #  1 = input number 2 = fixed number 0 = wrong number
               [1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1],]

def load_sudoku(filename): # load numbers from text file
    global table
    nums = loadStrings(filename) # nums for load numbers form text file
    for num in nums:
        rows = [] # rows for rows in nums
        for n in num: # n for each column in num
            rows.append(int(n)) # add int n to rows
        table.append(rows) # add rows to table
        
    for i in range(9):
        for j in range(9):
            if table[i][j] != 0: # if number in text file is not equal 0
                truth_value[i][j] = 2 # It is a fixed number

def draw_num(): # draw numbers from table
    global table
    for i in range(9):
        for j in range(9):
            if table[i][j] != 0: # check if table is not empty
                if truth_value[i][j] == 2: # fixed number fill black
                    fill(0)
                elif truth_value[i][j] == 1: # input number fill blue
                    fill(0,0,200)
                else: # wrong number fill red
                    fill(200,0,0)
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
    clicked_rows = rows # clicked rows = rows
    clicked_cols = cols # clicked cols = cols
        
def keyPressed(): # input number
    if clicked_rows != -1 and clicked_cols != -1: # check if cell_size is unclicked
        if truth_value[clicked_rows][clicked_cols] != 2: # if number is not fixed number
            if key >= '1' and key <= '9': # if keyboard between 1 to 9
                table[clicked_rows][clicked_cols] = int(key) # number in table = int(ket)
                checkNum() # call checkNum()
            elif key == BACKSPACE: # if key is BACKSPACE
                table[clicked_rows][clicked_cols] = 0 # delete number
                truth_value[clicked_rows][clicked_cols] = 1 # number is input number

def checkNum():
    global table,clicked_rows,clicked_cols,truth_value
    for i in range(9):
        if table[clicked_rows][clicked_cols] == table[i][clicked_cols] and i != clicked_rows: # check each column
            truth_value[clicked_rows][clicked_cols] = 0
    
    for j in range(9):
        if table[clicked_rows][clicked_cols] == table[clicked_rows][j] and j != clicked_cols: # check each rows
            truth_value[clicked_rows][clicked_cols] = 0
        
    s_rows = (clicked_rows // 3) * 3 # s_rows for start rows
    s_cols = (clicked_cols // 3) * 3 # s_cols for start columns
    for i in range(3):
        for j in range(3):
            r = s_rows + i
            c = s_cols + j
            if table[clicked_rows][clicked_cols] == table[r][c] and (r != clicked_rows or c != clicked_cols): # if number is equal other number in block 3x3
                truth_value[clicked_rows][clicked_cols] = 0 # It is a wrong number
    
def setup():
    size(width,height) 
    load_sudoku("sudoku.txt") # load sudoku numbers
    textAlign(CENTER,CENTER) # set text to center
    textSize(20) # size of text
    
def draw():
    background(200)
    draw_table() # draw sudoku table
    draw_num()  # draw numbers from table
    if clicked_rows != -1 and clicked_cols != -1: # if mouse is clicked
        fill(0,200,0,100)
        rect(clicked_cols * cell_size, clicked_rows * cell_size, cell_size, cell_size) # draw green square

            
            
            
            
