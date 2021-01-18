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
    print("{0:2} {1}".format(i, colours[i]))
    blinkt.set_all(colours[i][0], colours[i][1], colours[i][2])
    blinkt.show()
    time.sleep(1)

def show_flp(unix_time):
    fourletterphat.clear()
    time_string = time.strftime("%H%M", time.localtime(unix_time))
    fourletterphat.print_number_str(time_string)
    fourletterphat.set_decimal(1, int(unix_time % 2))
    fourletterphat.show()

def show_binary(num, r, g, b):
    n = int(num) & 0xFF
    bit = 0x01
    for i in range(0, 8):
        if n & bit > 0:
            blinkt.set_pixel(7 - i, r, g, b)
        else:
            blinkt.set_pixel(7 - i, 0, 0, 0)
        bit = bit << 1
    blinkt.show()

def show_blinkt(unix_time):
    l = time.localtime(unix_time)
    # only enable blinkt between 08:00 and 21:00
    if l.tm_hour > 7 and l.tm_hour < 21:
        colour = colours[l.tm_min % len(colours)]
        show_binary(unix_time, colour[0], colour[1], colour[2])
    else:
        blinkt.set_all(0, 0, 0)
        blinkt.show()

while True:
    unix_time = time.time()
    show_flp(unix_time)
    show_blinkt(unix_time)
    time.sleep(0.1)

