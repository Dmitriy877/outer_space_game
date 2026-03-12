import time
import curses
import asyncio
import random

TIC_TIMEOUT = 0.1
SYMBOLS = ['+', '*', '.', ':']
STARS_AMOUNT = 100


def draw(canvas):
    curses.curs_set(0)
    canvas.border()
    coroutines = list()
    max_y, max_x = canvas.getmaxyx()

    fire_coroutine = fire(canvas, max_y//2, max_x//2)
    coroutines.append(fire_coroutine)

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


async def fire(canvas, start_row, start_column, rows_speed=-0.3, columns_speed=0):
    """Display animation of gun shot, direction and speed can be specified."""

    row, column = start_row, start_column

    canvas.addstr(round(row), round(column), '*')
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), 'O')
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), ' ')

    row += rows_speed
    column += columns_speed

    symbol = '-' if columns_speed else '|'

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), ' ')
        row += rows_speed
        column += columns_speed


async def blink(canvas, row, column, symbol='*'):
    while True:
        for i in range(random.randint(1, 50)):
            canvas.addstr(row, column, symbol, curses.A_DIM)
            await asyncio.sleep(0)

        for i in range(random.randint(1, 50)):
            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)

        for i in range(random.randint(1, 50)):
            canvas.addstr(row, column, symbol, curses.A_BOLD)
            await asyncio.sleep(0)

        for i in range(random.randint(1, 50)):
            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)