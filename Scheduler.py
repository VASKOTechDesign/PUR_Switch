def Schedule_Cerpadlo(DB_SET, display):
    def Time_dif(H_From, M_From, H_To, M_To):
        import utime
        Time_From = utime.mktime([2020, 1, 1, 0, H_From, M_From, 0, 0])
        Time_To = utime.mktime([2020, 1, 1, 0, H_To, M_To , 0, 0])
        Difference = (Time_To - Time_From)*60*1000
        print("Difference Counted: "+str(Difference))
        return Difference

    def Morning_Period(pin):
        print("Morning Cerpadlo - Timer")
        import utime
        import machine
        import btree
        rtc = machine.RTC()

        f_SET = open("Database/Settings.db", "r+b")
        DB_SET = btree.open(f_SET)
        Z1_T_From_H = int(DB_SET[str(0)].decode('utf-8'))
        Z1_T_From_M = int(DB_SET[str(1)].decode('utf-8'))
        Z1_T_To_H = int(DB_SET[str(2)].decode('utf-8'))
        Z1_T_To_M = int(DB_SET[str(3)].decode('utf-8'))
        Cerpadlo_Process = int(DB_SET[str(5)].decode('utf-8'))*60    # [seconds]
        Page = int(DB_SET[str(30)].decode('utf-8'))
        DB_SET.close()
        f_SET.close()

        Time_Act = rtc.datetime()
        Time_From = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z1_T_From_H, Z1_T_From_M, 0, 0])
        Time_To = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z1_T_To_H, Z1_T_To_M , 0, 0])
        Time_Act = utime.mktime(rtc.datetime())

        if (Page == 1) or (Page == 0) and ((Time_Act>Time_From) and (Time_Act<Time_To)):
            Cerpadlo = machine.Pin(4, machine.Pin.OUT)
            Cerpadlo.on()
            print("Morning - ON")
            utime.sleep(Cerpadlo_Process)
            print("Morning - Off")
            Cerpadlo.off()

    def Day_Period(pin):
        print("Day Cerpadlo - Timer")
        import utime
        import machine
        import btree
        rtc = machine.RTC()

        f_SET = open("Database/Settings.db", "r+b")
        DB_SET = btree.open(f_SET)
        Z2_T_From_H = int(DB_SET[str(6)].decode('utf-8'))
        Z2_T_From_M = int(DB_SET[str(7)].decode('utf-8'))
        Z2_T_To_H = int(DB_SET[str(8)].decode('utf-8'))
        Z2_T_To_M = int(DB_SET[str(9)].decode('utf-8'))
        Cerpadlo_Process = int(DB_SET[str(11)].decode('utf-8'))*60    # [seconds]
        Page = int(DB_SET[str(30)].decode('utf-8'))
        DB_SET.close()
        f_SET.close()

        Time_Act = rtc.datetime()
        Time_From = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z2_T_From_H, Z2_T_From_M, 0, 0])
        Time_To = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z2_T_To_H, Z2_T_To_M , 0, 0])
        Time_Act = utime.mktime(rtc.datetime())

        if (Page == 1) or (Page == 0) and ((Time_Act>Time_From) and (Time_Act<Time_To)):
            Cerpadlo = machine.Pin(4, machine.Pin.OUT)
            Cerpadlo.on()
            print("Day - ON")
            utime.sleep(Cerpadlo_Process)
            print("Day - Off")
            Cerpadlo.off()

    def Evening_Period(pin):
        print("Evening Cerpadlo - Timer")
        import utime
        import machine
        import btree
        rtc = machine.RTC()

        f_SET = open("Database/Settings.db", "r+b")
        DB_SET = btree.open(f_SET)
        Z3_T_From_H = int(DB_SET[str(12)].decode('utf-8'))
        Z3_T_From_M = int(DB_SET[str(13)].decode('utf-8'))
        Z3_T_To_H = int(DB_SET[str(14)].decode('utf-8'))
        Z3_T_To_M = int(DB_SET[str(15)].decode('utf-8'))
        Cerpadlo_Process = int(DB_SET[str(17)].decode('utf-8'))*60    # [seconds]
        Page = int(DB_SET[str(30)].decode('utf-8'))
        DB_SET.close()
        f_SET.close()

        Time_Act = rtc.datetime()
        Time_From = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z3_T_From_H, Z3_T_From_M, 0, 0])
        Time_To = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z3_T_To_H, Z3_T_To_M , 0, 0])
        Time_Act = utime.mktime(rtc.datetime())

        if (Page == 1) or (Page == 0) and ((Time_Act>Time_From) and (Time_Act<Time_To)):
            Cerpadlo = machine.Pin(4, machine.Pin.OUT)
            Cerpadlo.on()
            print("Evening - ON")
            utime.sleep(Cerpadlo_Process)
            print("Evening - Off")
            Cerpadlo.off()

    def Filter_Period(pin):
        import utime
        import machine
        import btree
        import bitmapfont
        Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")

        f_SET = open("Database/Settings.db", "r+b")
        DB_SET = btree.open(f_SET)
        Filtr_Process = int(DB_SET[str(41)].decode('utf-8'))*60    # [seconds]
        Page = int(DB_SET[str(30)].decode('utf-8'))
        DB_SET.close()
        f_SET.close()

        if (Page == 1) or (Page == 0):
            Filtrace = machine.Pin(15, machine.Pin.OUT)
            Font1.init()
            Font1.text("Filter Run", 1, 1, 1, 1)
            Filtrace.on()
            utime.sleep(Filtr_Process)
            Filtrace.off()
            display.fill_rectangle(0, 0, 10, 149, 0xf7be)
            Font1.text("Ready", 1, 1, 1, 1)
            Font1.deinit()
        print("Filter Timer - process")

    import machine
    tim0 = machine.Timer(0) # Morning
    tim1 = machine.Timer(1) # Day
    tim2 = machine.Timer(2) # Evening
    tim3 = machine.Timer(4) # Filter
    try:
        tim0.deinit()
        tim1.deinit()
        tim2.deinit()
        tim3.deinit()
    except:
        pass

    #-------------Cerpadlo - Morning-------------#
    # Set schedule timer in miliseconds
    Z1_T_From_H = int(DB_SET[str(0)].decode('utf-8'))
    Z1_T_From_M = int(DB_SET[str(1)].decode('utf-8'))
    Z1_T_To_H = int(DB_SET[str(2)].decode('utf-8'))
    Z1_T_To_M = int(DB_SET[str(3)].decode('utf-8'))
    Z1_Cerpadlo_Count = int(DB_SET[str(4)].decode('utf-8'))

    Differnece_M = Time_dif(Z1_T_From_H, Z1_T_From_M, Z1_T_To_H, Z1_T_To_M)
    SCHED_TIME0 = round(Differnece_M / Z1_Cerpadlo_Count)    # [mili-seconds]

    #Timer
    tim0 = machine.Timer(0)
    tim0.init(mode=machine.Timer.PERIODIC, period=SCHED_TIME0, callback=Morning_Period)
    print("Morning Cerpadlo Timer Setuped")

    #-------------Cerpadlo - Day-------------#
    # Set schedule timer in miliseconds
    Z2_T_From_H = int(DB_SET[str(6)].decode('utf-8'))
    Z2_T_From_M = int(DB_SET[str(7)].decode('utf-8'))
    Z2_T_To_H = int(DB_SET[str(8)].decode('utf-8'))
    Z2_T_To_M = int(DB_SET[str(9)].decode('utf-8'))
    Z2_Cerpadlo_Count = int(DB_SET[str(10)].decode('utf-8'))

    Differnece_D = Time_dif(Z2_T_From_H, Z2_T_From_M, Z2_T_To_H, Z2_T_To_M)
    SCHED_TIME1 = round(Differnece_D / Z2_Cerpadlo_Count)    # [mili-seconds]

    #Timer
    tim1 = machine.Timer(1)
    tim1.init(mode=machine.Timer.PERIODIC, period=SCHED_TIME1, callback=Day_Period)
    print("Day Cerpadlo Timer Setuped")

    #-------------Cerpadlo - Evening-------------#
    # Set schedule timer in miliseconds
    Z3_T_From_H = int(DB_SET[str(12)].decode('utf-8'))
    Z3_T_From_M = int(DB_SET[str(13)].decode('utf-8'))
    Z3_T_To_H = int(DB_SET[str(14)].decode('utf-8'))
    Z3_T_To_M = int(DB_SET[str(15)].decode('utf-8'))
    Z3_Cerpadlo_Count = int(DB_SET[str(16)].decode('utf-8'))

    Differnece_E = Time_dif(Z3_T_From_H, Z3_T_From_M, Z3_T_To_H, Z3_T_To_M)
    SCHED_TIME2 = round(Differnece_E / Z3_Cerpadlo_Count)    # [mili-seconds]

    #Timer
    tim2 = machine.Timer(2)
    tim2.init(mode=machine.Timer.PERIODIC, period=SCHED_TIME2, callback=Evening_Period)
    print("Evening Cerpadlo Timer Setuped")
    machine.reset()

    #-------------Filter-------------#
    # Count function how many times run / day
    Filtr_Count = int(DB_SET[str(40)].decode('utf-8'))
    SCHED_TIME3 = round(24 / Filtr_Count * 60 * 60 * 1000)    # [mili-seconds]
    DB_SET[str(51)] = str(SCHED_TIME3)
    DB_SET.flush()

    #Timer
    tim3 = machine.Timer(3)
    tim3.init(mode=machine.Timer.PERIODIC, period=SCHED_TIME3, callback=Filter_Period)
