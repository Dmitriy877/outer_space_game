import asyncio
import curses
from .curses_tools import draw_frame

GAME_OVER_FRAME = [
    """\
    _____                        ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      
    """]


async def show_gameover(canvas):
    max_y, max_x = canvas.getmaxyx()

    curses.beep()
    while True:

        draw_frame(canvas, max_y//2-5, max_x//2 - 25, GAME_OVER_FRAME[0])
        await asyncio.sleep(0)
