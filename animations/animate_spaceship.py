import itertools
import asyncio

from .curses_tools import draw_frame, read_controls


async def animate_spaceship(
                            canvas,
                            start_row,
                            start_column,
                            animation_1,
                            animation_2
):

    frames = [animation_1, animation_2]
    frame_cycler = itertools.cycle(frames)

    while True:
        rows_direction, columns_direction, space_pressed = read_controls(canvas)
        start_row += rows_direction
        start_column += columns_direction
        current_frame = next(frame_cycler)
        draw_frame(canvas, start_row, start_column, current_frame)
        canvas.refresh()
        await asyncio.sleep(0)
        draw_frame(canvas, start_row, start_column, current_frame, negative=True)

