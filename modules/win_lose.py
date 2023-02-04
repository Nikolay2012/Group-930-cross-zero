import modules.create_line as m_line

def gorizontal_win(list_cell, number):
    if list_cell[0] == number and list_cell[1] == number and list_cell[2] == number:
        m_line.draw_line(-50, 50)
    elif list_cell[3] == number and list_cell[4] == number and list_cell[5] == number:
        m_line.draw_line(-50, -50)
    elif list_cell[6] == number and list_cell[7] == number and list_cell[8] == number:
        m_line.draw_line(-50, -150)