def Filter_Period(pin):
    import utime
    import machine

    Filtrace = machine.Pin(15, machine.Pin.OUT)
    Filtrace.on()
    utime.sleep(1)
    Filtrace.off()

    print("Filter Timer - process")

print("Getting Timer for Filter Starts")

import machine
import btree

tim3 = machine.Timer(3)
try:
    tim3.deinit()
except:
    pass

f_SET = open("Database/Settings.db", "r+b")
DB_SET = btree.open(f_SET)

# Count function how many times run / day
Filtr_Count = int(DB_SET[str(40)].decode('utf-8'))
SCHED_TIME3 = round(24 / Filtr_Count * 60 * 60 * 1000)    # [mili-seconds]
DB_SET[str(51)] = str(SCHED_TIME3)
DB_SET.flush()
DB_SET.close()
f_SET.close()

#Timer
tim3 = machine.Timer(3)
tim3.init(mode=machine.Timer.PERIODIC, period=2520, callback=Filter_Period)
