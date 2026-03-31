import random
import asyncio

from .space_garbage import fly_garbage
from .sleep import sleep


async def fill_orbit_with_garbage(canvas, coroutines, obstacles):
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
        coroutines.append(fly_garbage(canvas, random.randint(1, max_x - 1), garbage_frame, obstacles))
        await sleep(10)