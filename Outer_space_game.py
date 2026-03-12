import time
import curses
import asyncio
import random

TIC_TIMEOUT = 0.1
SYMBOLS = ['+', '*', '.', ':']
STARS_AMOUNT = 100


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    coroutines = list()
    max_y, max_x = canvas.getmaxyx()

    for i in range(STARS_AMOUNT):
        row = random.randint(2, max_y - 2)
        column = random.randint(2, max_x - 2)
        symbol = random.choice(SYMBOLS)
        coroutines.append(blink(canvas, row, column, symbol))

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
                canvas.refresh()
            except StopIteration:
                coroutines.remove(coroutine)
        canvas.refresh()

        time.sleep(TIC_TIMEOUT)

        if len(coroutines) == 0:
            break


async def blink(canvas, row, column, symbol='*'):
    while True:
        for i in range(20):
            canvas.addstr(row, column, symbol, curses.A_DIM)
            await asyncio.sleep(0)

        for i in range(3):
            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)

        for i in range(5):
            canvas.addstr(row, column, symbol, curses.A_BOLD)
            await asyncio.sleep(0)

        for i in range(3):
            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)