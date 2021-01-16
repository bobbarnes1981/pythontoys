import blinkt
import fourletterphat
import psutil
import time

blinkt.set_clear_on_exit(True)
blinkt.set_brightness(0.05)

fourletterphat.clear()

print("BLINKT PIXELS {0}".format(blinkt.NUM_PIXELS))

fourletterphat.print_str('AHOY')
fourletterphat.show()

colours = [
    [255, 255, 255],    # white
    [255, 0, 0],        # red
    [255, 127, 0],      # orange
    [255, 255, 0],      # yellow
    [0, 255, 0],        # green
    [0, 0, 255],        # blue
    [0, 255, 255],      # sky blue?
    [255, 0, 127],      # fuscia
]

for i in range(0, len(colours)):
    blinkt.set_all(colours[i][0], colours[i][1], colours[i][2])
    blinkt.show()
    time.sleep(1)

def show_flp():
    fourletterphat.clear()
    str_time = time.strftime("%H%M")
    fourletterphat.print_number_str(str_time)
    fourletterphat.set_decimal(1, int(time.time() % 2))
    fourletterphat.show()

def show_blinkt():
    t = time.time()
    l = time.localtime(t)
    if l.tm_hour > 7 and l.tm_hour < 21:
        t = int(t) & 0xFF
        b = 0x01
        # pick a colour
        colour = colours[l.tm_min % len(colours)]
        for i in range(0, 8):
            if t & b > 0:
                blinkt.set_pixel(7 - i, colour[0], colour[1], colour[2])
            else:
                blinkt.set_pixel(7 - i, 0, 0, 0)
            b = b << 1
        blinkt.show()
    else:
        blinkt.set_all(0, 0, 0)
        blinkt.show()

while True:
    show_flp()
    show_blinkt()
    time.sleep(0.1)

