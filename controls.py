from nxt.motor import Motor
from time import time, sleep
import asyncio
import math
import numpy as np


class Controls:
    def __init__(self, lmotor: Motor, rmotor: Motor) -> None:
        self.RADIUS = 10
        self.motors: tuple[Motor, Motor] = (lmotor, rmotor)
        # self.directon: list[int, int] = [1, 0] # straigt
        self.time_since_last = -1
        self.time = time()
        self.speed = np.array([0, 0])

        self.debug = True

        self.left = 0
        self.right = 0

    async def change_speed(self, i: int, j: int) -> None:
        """[-100, 100]"""
        if not self.debug:
            self.motors[0].run(power=i)
            self.motors[1].run(power=j)

        self.speed[0] = i
        self.speed[1] = j

    async def turn_angle(self, angle: float, ratio=2, speed=100) -> None:
        """
        angle: [-180, 180]
        ratio: ]1; 100]
        """
        slow = round(speed / ratio)

        if angle > 0:
            await self.change_speed(slow, speed)
        elif angle < 0:
            await self.change_speed(speed, slow)
        elif angle == 0:
            await self.change_speed(speed, speed)
            return
        else:
            return

        s = math.pi * 2 * self.RADIUS
        v = speed - slow
        t = s / v
        print(f"sleeping {t}s")
        await asyncio.sleep(t)
        await self.change_speed(100, 100)
        print("fin")

    async def tick(self):
        current = time()
        self.time_since_last = current - self.time
        self.time = current

        self.left += self.speed[0]*self.time_since_last
        self.right += self.speed[1]*self.time_since_last
        # print(self.left-self.right)
        print(self.speed)


async def main():
    controls = Controls(None, None)
    await controls.change_speed(50, 50)

    for _ in range(30):
        sleep(.1)
        await controls.tick()

    await controls.turn_angle(90)

    while True:
        await controls.tick()
        sleep(.1)

if __name__ == "__main__":
    asyncio.run(main=main())
