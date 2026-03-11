import time
import curses
import asyncio


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    row, column = (5, 20)
    coroutine = blink(canvas, row, column)
    while True:
        try:
            time.sleep(0.3)
            coroutine.send(None)
            canvas.refresh()
        except StopAsyncIteration:
            break
    time.sleep(3)


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