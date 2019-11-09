#  Gamepad controller handling library
#
#  Bluetooth pairing via command line:
#  https://bluedot.readthedocs.io/en/latest/pairpipi.html#using-the-command-line

from evdev import InputDevice, ecodes
import asyncio

# event3 is specific to my controller, yours may be different
dev = InputDevice('/dev/input/event3')

async def helper(dev):
    async for ev in dev.async_read_loop():
        print(repr(ev))

loop = asyncio.get_event_loop()
loop.run_until_complete(helper(dev))