from time import sleep
import asyncio
from controls import Controls
from nxt.motor import Motor
from brick import get_nxt, Port
from nxt.brick import Brick


async def main():
    # nxt connection
    nxt: Brick = get_nxt()

    # motor controls
    lmotor = Motor(nxt, Port.D)
    rmotor = Motor(nxt, Port.G)

    # init controls
    controls = Controls(lmotor, rmotor)

    # set initial speed
    await controls.change_speed(50, 50)

    # wait 3 seconds
    sleep(3)

    # turn 90 degree with curren speed (maybe adjust speed)
    await controls.turn_angle(90)

    # infinit loop (keep programm running)
    while True:
        # for calculating data in controls object (timedelta)
        await controls.tick()

        # sleep 0.1s
        sleep(.1)


if __name__ == "__main__":
    asyncio.run(main=main())
