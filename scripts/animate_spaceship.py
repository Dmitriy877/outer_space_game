import itertools
import asyncio

from .curses_tools import draw_frame, read_controls, get_frame_size
from .fire import fire
from .show_gameover import show_gameover
from .show_message import show_message

PHRASES = {
    1957: "First Sputnik",
    1961: "Gagarin flew!",
    1969: "Armstrong got on the moon!",
    1971: "First orbital space station Salute-1",
    1981: "Flight of the Shuttle Columbia",
    1998: 'ISS start building',
    2011: 'Messenger launch to Mercury',
    2020: "Take the plasma gun! Shoot the garbage!",
}


async def animate_spaceship(
                            canvas,
                            start_row: int,
                            start_column: int,
                            animation_1: str,
                            animation_2: str,
                            coroutines: list,
                            obstacles: list,
                            obstacles_in_last_collision: list,
                            year: list
) -> None:

    max_rows, max_columns = canvas.getmaxyx()
    frames = [animation_1, animation_1, animation_2, animation_2]
    frame_cycler = itertools.cycle(frames)

    ship_height, ship_width = get_frame_size(animation_1)

    shown_messages = set()

    while True:

        for obstacle in obstacles:
            if obstacle.has_collision(start_row, start_column, ship_width, ship_height):
                coroutines.append(show_gameover(canvas))
                return

        rows_direction, columns_direction, space_pressed = read_controls(canvas)

        start_row += rows_direction
        start_column += columns_direction

        if start_row < 1:
            start_row = 1

        if start_row > max_rows - ship_height - 1:
            start_row = max_rows - ship_height - 1

        if start_column < 1:
            start_column = 1

        if start_column > max_columns - ship_width - 1:
            start_column = max_columns - ship_width - 1

        current_frame = next(frame_cycler)

        if year[0] in PHRASES.keys() and year[0] not in shown_messages:
            shown_messages.add(year[0])
            coroutines.append(show_message(canvas, f"{year[0]:} {PHRASES[year[0]]}"))

        if year[0] >= 2020:
            if space_pressed:
                coroutines.append(fire(canvas, start_row, start_column+2, obstacles, obstacles_in_last_collision))

        draw_frame(canvas, start_row, start_column, current_frame)
        await asyncio.sleep(0)
        draw_frame(canvas, start_row, start_column, current_frame, negative=True)