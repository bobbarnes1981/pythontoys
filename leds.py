import blinkt
import time

blinkt.set_clear_on_exit(True)
blinkt.set_brightness(0.05)

print("BLINKT {0}".format(blinkt.NUM_PIXELS))

blinkt.set_all(255, 0, 0)
blinkt.show()
time.sleep(1)
blinkt.set_all(0, 255, 0)
blinkt.show()
time.sleep(1)
blinkt.set_all(0, 0, 255)
blinkt.show()
time.sleep(1)

while True:
    t = time.time()
    l = time.localtime(t)
    if l.tm_hour > 7 and l.tm_hour < 21:
        t = int(t) & 0xFF
        b = 0x01
        for i in range(0, 8):
            if t & b > 0:
                blinkt.set_pixel(7 - i, 255, 255, 255)
            else:
                blinkt.set_pixel(7 - i, 0, 0, 0)
            b = b << 1
        blinkt.show()
        time.sleep(0.1)
    else:
        blinkt.set_all(0, 0, 0)
        blinkt.show()
        time.sleep(60)

