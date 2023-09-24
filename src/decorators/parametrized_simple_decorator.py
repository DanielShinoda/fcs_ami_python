from clock.parametrized_clock import clock
import time


@clock()
def snooze(seconds) -> None:
    time.sleep(seconds)

# @clock('{name}: {elapsed}s')
# def snooze(seconds) -> None:
#     time.sleep(seconds)

# @clock('{name}({args}) dt={elapsed:0.3f}s')
# def snooze(seconds) -> None:
#     time.sleep(seconds)


for i in range(3):
    snooze(0.123)
