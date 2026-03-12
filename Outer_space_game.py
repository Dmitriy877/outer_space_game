import time
import curses
import asyncio


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    coroutines = [
        blink(canvas, 5, 21),
        blink(canvas, 5, 22),
        blink(canvas, 5, 23),
        blink(canvas, 5, 24),
        blink(canvas, 5, 25),
    ]

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
                canvas.refresh()
            except StopIteration:
                coroutines.remove(coroutine)
        canvas.refresh()
        if len(coroutines) == 0:
            break


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)