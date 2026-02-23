from robot import *

while is_free_right():
    move_right()
    if(is_cell_painted()):
        move_right()
        paint()