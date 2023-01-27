import time

from machine import Pin

SLEEP_TIME = 100
BLINK_TIMES = 4


def blink(led: Pin):
    for _ in range(BLINK_TIMES):
        led.on()
        time.sleep_ms(SLEEP_TIME)
        led.off()
        time.sleep_ms(SLEEP_TIME)
    led.off()
