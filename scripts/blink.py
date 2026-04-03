import curses

from .sleep import sleep


async def blink(canvas, row: int,
                column: int,
                symbol='*',
                offset_tics=0
                ) -> None:
    await sleep(offset_tics)

    while True:
        await sleep(20)
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await sleep(3)
        canvas.addstr(row, column, symbol)
        await sleep(5)
        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await sleep(3)
        canvas.addstr(row, column, symbol)