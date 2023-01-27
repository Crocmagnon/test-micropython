from machine import Pin
import network
from microdot_asyncio import Microdot

from somelib.module import blink

app = Microdot()

led = Pin("LED", Pin.OUT)

@app.route('/')
async def index(request):
    blink(led)
    return 'Hello, world!'


nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect("ssid", "password")

blink(led)
app.run()
