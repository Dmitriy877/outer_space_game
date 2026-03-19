import curses
import asyncio


async def blink(canvas, row, column, symbol='*', offset_tics=0):
    for _ in range(offset_tics):
        await asyncio.sleep(0)

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