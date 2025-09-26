clicked_rows = -1 # empty rows 
clicked_cols = -1 # empty cols
cell_size = 67 # size of cell

def draw_table():
    for i in range(8):
        strokeWeight(1)
        if i == 2 or i== 5:
            strokeWeight(2)
        line(67+67*i,0,67+67*i,height)
        
    for i in range(8):
        strokeWeight(1)
        if i == 2 or i== 5:
            strokeWeight(2)
        line(0,67+67*i,width,67+67*i)

def mousePressed():
    global clicked_rows,clicked_cols
    rows = floor(mouseY/ cell_size)
    cols = floor(mouseX / cell_size)
    if (rows >= 0 and rows < 9) and (cols >= 0 and cols < 9):
        clicked_rows = rows
        clicked_cols = cols
        
def setup():
    size(600,600)
    
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
    
            
