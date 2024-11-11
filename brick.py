from nxt.locator import find
from nxt.brick import Brick
from nxt.motor import Port as port_m
from nxt.sensor import Port as port_s
from enum import Enum


class Port(Enum):
    A = port_m("0")
    B = port_m("1")
    C = port_m("2")
    D = port_s("3")
    E = port_s("4")
    F = port_s("5")
    G = port_s("6")


def get_nxt(timeout: int = 3) -> Brick | None:
    NXT_MAC = ""
    for _ in range(timeout):
        brick: Brick = find(name="NXT", host=NXT_MAC)
        if brick:
            return brick
        print("didn't find break, trying again. Please Turn on the NXT!")
