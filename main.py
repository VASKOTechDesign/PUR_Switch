#/-----------------------Display IRQ functions-----------------------/#
#Display
def touch_ON(pin):
    #Touch
    ts_cs.off()
    stisk = ts_touch.raw_touch()
    ts_cs.on()
    tft_cs.off()

    #Search
    import Find_Page_mod
    if stisk!=None:
        Find_Page_mod._1_Find_Page(stisk, display)

    tft_cs.on()
    ts_cs.off()

#/-------------------------Schedule functions-------------------------/#
def Dispaly_OFF(pin):
    print("Timer Log.: Display-OFF")
    f_SET = open("Database/Settings.db", "r+b")
    DB_SET = btree.open(f_SET)

    Page = int(DB_SET[str(30)].decode('utf-8'))
    if Page == 1:
        DB_SET[str(30)] = "0"
        DB_SET.flush()
        import machine
        ts_LED = machine.Pin(32, machine.Pin.OUT)
        ts_LED.off()
    DB_SET.close()
    f_SET.close()

def Display_Act_Time(pin):
    print("Timer Log.: Active Time")
    f_SET = open("Database/Settings.db", "r+b")
    DB_SET = btree.open(f_SET)
    Page = int(DB_SET[str(30)].decode('utf-8'))
    if (Page == 1) or (Page == 0):
        # Načíst RTC
        import machine
        rtc = machine.RTC()
        now = rtc.datetime()

        RTC = str(now[2])+"."+str(now[1])+"."+str(now[0])+" "+str(now[4])+":"+str(now[5])

        import bitmapfont
        Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")
        display.fill_rectangle(1, 151, 9, 105, 0xdedb)

        Font1.init()
        Font1.text(RTC, 155, 1, 1, 1)
        Font1.deinit()

    DB_SET.close()
    f_SET.close()

def Restart(pin):
    print("Timer Log.: Restart Machine")
    import machine
    machine.reset()

#Setup
import gc
import machine
import btree

tft_cs.on()
ts_cs.off()

#/-------------------------Initialize Display-------------------------/#
display.fill_rectangle(0, 0, 10, 149, 0xf7be)
import bitmapfont
Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")
Font1.init()
Font1.text("Initialize screen...", 1, 1, 1, 1)
display.fill_rectangle(0, 0, 10, 149, 0xf7be)
Font1.text("Ready", 1, 1, 1, 1)
Font1.deinit()

#/-----------------------------IRQ-----------------------------/#
#Display
ts_bussy.irq(handler=touch_ON)

#/------------------------Schedule------------------------/#
f_SET = open("Database/Settings.db", "r+b")
DB_SET = btree.open(f_SET)

#Display - Off
SCHED_TIME4 = int(DB_SET[str(52)].decode('utf-8'))
tim4 = machine.Timer(4)
tim4.init(mode=machine.Timer.PERIODIC, period=SCHED_TIME4, callback=Dispaly_OFF)

#Display - Actula Date and Time
SCHED_TIME5 = int(DB_SET[str(53)].decode('utf-8'))
tim5 = machine.Timer(5)
tim5.init(mode=machine.Timer.PERIODIC, period=SCHED_TIME5, callback=Display_Act_Time)

#Restart
SCHED_TIME6 = int(DB_SET[str(54)].decode('utf-8'))
tim6 = machine.Timer(6)
tim6.init(mode=machine.Timer.PERIODIC, period=SCHED_TIME6, callback=Restart)

DB_SET.close()
f_SET.close()

gc.collect()
gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
