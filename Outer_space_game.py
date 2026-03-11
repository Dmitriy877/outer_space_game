import time
import curses


def draw(canvas):
    while True:
        row, column = (5, 20)

        canvas.addstr(row, column, '*', curses.A_DIM)
        canvas.border()
        time.sleep(1)
        canvas.refresh()
        curses.curs_set(False)

        canvas.addstr(row, column, '*')
        canvas.border()
        time.sleep(0.3)
        canvas.refresh()
        curses.curs_set(False)

        canvas.addstr(row, column, '*', curses.A_BOLD)
        canvas.border()
        time.sleep(0.5)
        canvas.refresh()
        curses.curs_set(False)

        canvas.addstr(row, column, '*')
        canvas.border()
        time.sleep(0.3)
        canvas.refresh()
        curses.curs_set(False)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)