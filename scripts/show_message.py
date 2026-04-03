import curses

from .curses_tools import draw_frame
from .sleep import sleep


async def show_message(canvas, phrase):
    max_y, max_x = canvas.getmaxyx()
    curses.beep()

    row = max_y - 3
    col = max_x - len(phrase) - 2

    draw_frame(canvas, row, col, phrase)
    await sleep(50)

    draw_frame(canvas, row, col, phrase, negative=True)