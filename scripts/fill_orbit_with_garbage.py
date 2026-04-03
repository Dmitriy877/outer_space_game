import random
import asyncio

from .space_garbage import fly_garbage
from .sleep import sleep


async def fill_orbit_with_garbage(canvas, coroutines, obstacles, obstacles_in_last_collision, year):
    garbage_frames = [
        'duck',
        'hubble',
        'lamp',
        'trash_large',
        'trash_x1',
        'trash_small'
    ]

    garbage_animations = dict()
    for garbage_frame in garbage_frames:
        with open(f'frames/{garbage_frame}.txt', 'r') as garbage_animation:
            garbage_animations[garbage_frame] = garbage_animation.read()

    max_y, max_x = canvas.getmaxyx()

    while True:
        garbage_name = random.choice(garbage_frames)
        garbage_frame = garbage_animations[garbage_name]
        garbage_period = get_garbage_delay_tics(year)
        if not garbage_period:
            await asyncio.sleep(0)
        else:
            coroutines.append(fly_garbage(canvas, random.randint(1, max_x - 1), garbage_frame, obstacles, obstacles_in_last_collision, coroutines))
            await sleep(garbage_period)


def get_garbage_delay_tics(year):
    if year[0] < 1961:
        return None
    elif year[0] < 1969:
        return 20
    elif year[0] < 1981:
        return 14
    elif year[0] < 1995:
        return 10
    elif year[0] < 2010:
        return 8
    elif year[0] < 2020:
        return 6
    else:
        return 2




