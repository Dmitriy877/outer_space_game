import itertools
import asyncio

from .curses_tools import draw_frame, read_controls, get_frame_size


async def animate_spaceship(
                            canvas,
                            start_row,
                            start_column,
                            animation_1,
                            animation_2
):

    max_rows, max_columns = canvas.getmaxyx()
    frames = [animation_1, animation_1, animation_2, animation_2]
    frame_cycler = itertools.cycle(frames)

    ship_height, ship_width = get_frame_size(animation_1)

    while True:
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

        draw_frame(canvas, start_row, start_column, current_frame)
        await asyncio.sleep(0)
        draw_frame(canvas, start_row, start_column, current_frame, negative=True)

