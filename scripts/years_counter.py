from .sleep import sleep


async def years_counter(year):
    while True:
        await sleep(15)
        year[0] += 1
