from .curses_tools import draw_frame
import asyncio

from .obstacles import Obstacle
from .curses_tools import get_frame_size
from .explosion import EXPLOSION_FRAMES, explode


async def fly_garbage(canvas, column, garbage_frame, obstacles, obstacles_in_last_collision, coroutines, speed=0.5,):
    """Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start."""
    rows_number, columns_number = canvas.getmaxyx()

    column = max(column, 0)
    column = min(column, columns_number - 1)
    row = 0

    frame_rows, frame_columns = get_frame_size(garbage_frame)

    obstacle = Obstacle(row, column, frame_rows, frame_columns)
    obstacles.append(obstacle)
    while row < rows_number:
        if obstacle in obstacles_in_last_collision:
            coroutines.append(explode(canvas, row+3, column+3))
            obstacles.remove(obstacle)
            return

        draw_frame(canvas, row, column, garbage_frame)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, garbage_frame, negative=True)
        row += speed
        obstacle.row = row

    obstacles.remove(obstacle)