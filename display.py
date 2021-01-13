import time
import fourletterphat
import psutil

while True:
    fourletterphat.clear()

    str_time = time.strftime("%H%M")

    fourletterphat.print_number_str(str_time)

    fourletterphat.set_decimal(1, int(time.time() % 2))

#str_cpu = psutil.cpu_percent(None, False)

#fourletterphat.print_number_str(str_cpu)

    fourletterphat.show()

    time.sleep(0.1)

