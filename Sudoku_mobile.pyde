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
        
        
def setup():
    size(600,600)
    
def draw():
    draw_table()
