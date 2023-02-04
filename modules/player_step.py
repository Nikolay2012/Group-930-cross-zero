import modules.create_cross as m_cross
import modules.create_zero as m_zero
import modules.win_lose as m_win_lose
#
turn = ["cross"]
#
list_cell = [
    0, 0, 0, 
    0, 0, 0, 
    0, 0, 0
]
#
def whos_turn(x, y, number):
    if turn[0] == "cross" and list_cell[number] == 0:
        m_cross.draw_cross(x,y)
        list_cell[number] = 1
        m_win_lose.gorizontal_win(list_cell, 1)
        turn[0] = "zero"
        print(list_cell)
    elif turn[0] == "zero" and list_cell[number] == 0:
        m_zero.draw_zero(x + 50, y - 100)
        list_cell[number] = 2
        m_win_lose.gorizontal_win(list_cell, 2)
        turn[0] = "cross"
        print(list_cell)