from .sleep import sleep


async def years_counter(year: list) -> None:
    while True:
        await sleep(15)
        year[0] += 1
