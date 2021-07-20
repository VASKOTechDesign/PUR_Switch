#/----------------DRV8825 initiate correct value + FAN Turn Off----------------/#
import machine
import btree
Cerpadlo = machine.Pin(4, machine.Pin.OUT)
Cerpadlo.off()
Filtrace = machine.Pin(15, machine.Pin.OUT)
Filtrace.off()

#/-----------------------------Load Settings Data-----------------------------/#

try:
    f_SET = open("Database/Settings.db", "r+b")
    DB_SET = btree.open(f_SET)
    DB_SET[str(30)] = "1"   # Actual Display - in case of electry emergency turn Off to set it again as homescreen is first
    DB_SET[str(18)] = "0"   # Cerpadlo + Filtr - Enabled / not enabled 
    DB_SET.flush()
    DB_SET.close()
except:
    f_SET = open("Database/Settings.db", "w+b")
    DB_SET = btree.open(f_SET)

    DB_SET[str(0)] = "8"      # Zona1 - Time from (Hour)
    DB_SET[str(1)] = "00"     # Zona1 - Time from (Minute)
    DB_SET[str(2)] = "10"     # Zona1 - Time to (Hour)
    DB_SET[str(3)] = "00"     # Zona1 - Time to (Minute)
    DB_SET[str(4)] = "2"      # Zona1 - Count
    DB_SET[str(5)] = "2"      # Zona1 - Process time

    DB_SET[str(6)] = "10"     # Zona2 - Time from (Hour)
    DB_SET[str(7)] = "00"     # Zona2 - Time from (Minute)
    DB_SET[str(8)] = "17"     # Zona2 - Time to (Hour)
    DB_SET[str(9)] = "00"     # Zona2 - Time to (Minute)
    DB_SET[str(10)] = "10"    # Zona2 - Count
    DB_SET[str(11)] = "2"     # Zona2 - Process time

    DB_SET[str(12)] = "17"    # Zona3 - Time from (Hour)
    DB_SET[str(13)] = "00"    # Zona3 - Time from (Minute)
    DB_SET[str(14)] = "19"    # Zona3 - Time to (Hour)
    DB_SET[str(15)] = "00"    # Zona3 - Time to (Minute)
    DB_SET[str(16)] = "3"     # Zona3 - Count
    DB_SET[str(17)] = "2"     # Zona3 - Process time

    DB_SET[str(18)] = "0"     # Cerpadlo + filter Scheduled ON/OFF

    DB_SET[str(21)] = "2021"    # RTC - Year
    DB_SET[str(22)] = "07"      # RTC - Month
    DB_SET[str(23)] = "16"      # RTC - Day
    DB_SET[str(24)] = "08"      # RTC - Hour
    DB_SET[str(25)] = "00"      # RTC - Minute
    DB_SET[str(26)] = "2"       # RTC - Week Day
    DB_SET[str(27)] = "0"       # RTC - Set

    DB_SET[str(30)] = "1"   # Actual Display

    DB_SET[str(40)] = "4"   # Filter - per/Day
    DB_SET[str(41)] = "5"   # Filtr - Process Time

    DB_SET[str(50)] = "10000"   # Schedule - Cerpadlo [mili-seconds]
    DB_SET[str(51)] = "10000"   # Schedule - Filtrace [mili-seconds]
    DB_SET[str(52)] = "60000"   # Schedule - Display OFF [mili-seconds] - 1 minute
    DB_SET[str(53)] = "10000"   # Schedule - Display Actual Time [mili-seconds]
    DB_SET[str(54)] = "86400000"   # Schedule - Restart once per Day [mili-seconds]

    DB_SET[str(62)] = "0" # DB Initiation
    DB_SET.flush()
    DB_SET.close()

f_SET.close()

#/-----------------------------Display + Touch init-----------------------------/#
import gc
import sys
sys.path.insert(1, '/Lib')

import ili9341
import xpt2046
spi = machine.SPI(1, baudrate=2000000, polarity=0, phase=0, miso=machine.Pin(19), mosi=machine.Pin(23), sck=machine.Pin(18))
display = ili9341.ILI9341(spi, cs=machine.Pin(14), dc=machine.Pin(27), rst=machine.Pin(33))
ts_touch = xpt2046.XPT2046(spi = spi, confidence=5, margin=50, delay=10)

#Display
ts_bussy = machine.Pin(0, machine.Pin.IN)
ts_cs = machine.Pin(12, machine.Pin.OUT)
tft_cs = machine.Pin(14, machine.Pin.OUT)

tft_cs.off()
ts_cs.on()

#/-----------------------------Display Home Page-----------------------------/#
sys.path.insert(1, '/Display')
import _1_Home_Page_mod
_1_Home_Page_mod._1_Home_Page(display)

gc.collect()
gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
# Automatic Garbage collector
gc.enable()
