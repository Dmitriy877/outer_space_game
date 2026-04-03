import time
import curses
import random

from scripts.animate_spaceship import animate_spaceship
from scripts.blink import blink
from scripts.fill_orbit_with_garbage import fill_orbit_with_garbage
from scripts.obstacles import show_obstacles
from scripts.years_counter import years_counter


TIC_TIMEOUT = 0.1
SYMBOLS = ['+', '*', '.', ':']
STARS_AMOUNT = 100
year = [1957]
coroutines = list()
obstacles = list()
obstacles_in_last_collision = list()


def draw(canvas) -> None:
    with open('frames/rocket_frame_1.txt', 'r') as animation_file:
        rocket_frame_1 = animation_file.read()
    with open('frames/rocket_frame_2.txt', 'r') as animation_file:
        rocket_frame_2 = animation_file.read()

    curses.curs_set(0)
    canvas.nodelay(True)
    canvas.border()
    max_y, max_x = canvas.getmaxyx()

    years_frame = canvas.derwin(3, max_x - 2, max_y - 4, 1)

    coroutines.append(animate_spaceship(
        canvas,
        max_y//2,
        max_x//2,
        rocket_frame_1,
        rocket_frame_2,
        coroutines,
        obstacles,
        obstacles_in_last_collision,
        year
    ))
    coroutines.append(fill_orbit_with_garbage(canvas, coroutines, obstacles, obstacles_in_last_collision, year))
    coroutines.append(years_counter(year))

    for i in range(STARS_AMOUNT):
        offset_tics = random.randint(1, 50)
        row = random.randint(2, max_y - 2)
        column = random.randint(2, max_x - 2)
        symbol = random.choice(SYMBOLS)
        coroutines.append(blink(canvas, row, column, symbol, offset_tics))

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        years_frame.addstr(1, 1, f"year:{year}")
        canvas.refresh()
        years_frame.refresh()

        time.sleep(TIC_TIMEOUT)

        if len(coroutines) == 0:
            break
    years_frame.delwin()


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
