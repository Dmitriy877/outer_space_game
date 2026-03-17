import random
import curses
import asyncio


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