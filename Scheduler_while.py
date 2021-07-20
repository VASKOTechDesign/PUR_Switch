def Timer(DB_SET, display):
    import btree
    f_SET = open("Database/Settings.db", "r+b")
    DB_SET = btree.open(f_SET)
    Z1_T_From_H = int(DB_SET[str(0)].decode('utf-8'))
    Z1_T_From_M = int(DB_SET[str(1)].decode('utf-8'))
    Z1_T_To_H = int(DB_SET[str(2)].decode('utf-8'))
    Z1_T_To_M = int(DB_SET[str(3)].decode('utf-8'))
    Z1_Cerpadlo_Count = int(DB_SET[str(4)].decode('utf-8'))

    Z2_T_From_H = int(DB_SET[str(6)].decode('utf-8'))
    Z2_T_From_M = int(DB_SET[str(7)].decode('utf-8'))
    Z2_T_To_H = int(DB_SET[str(8)].decode('utf-8'))
    Z2_T_To_M = int(DB_SET[str(9)].decode('utf-8'))
    Z2_Cerpadlo_Count = int(DB_SET[str(10)].decode('utf-8'))

    Z3_T_From_H = int(DB_SET[str(12)].decode('utf-8'))
    Z3_T_From_M = int(DB_SET[str(13)].decode('utf-8'))
    Z3_T_To_H = int(DB_SET[str(14)].decode('utf-8'))
    Z3_T_To_M = int(DB_SET[str(15)].decode('utf-8'))
    Z3_Cerpadlo_Count = int(DB_SET[str(16)].decode('utf-8'))

    Z1_Cerpadlo_Process = int(DB_SET[str(5)].decode('utf-8'))*60      # [seconds]
    Z2_Cerpadlo_Process = int(DB_SET[str(11)].decode('utf-8'))*60     # [seconds]
    Z3_Cerpadlo_Process = int(DB_SET[str(17)].decode('utf-8'))*60     # [seconds]

    Filtr_Process = int(DB_SET[str(41)].decode('utf-8'))*60    # [seconds]
    Page = int(DB_SET[str(30)].decode('utf-8'))

    while (Page == 1) or (Page == 0):
        def Time_dif(H_From, M_From, H_To, M_To):
            import utime
            Time_From = utime.mktime([2020, 1, 1, 0, H_From, M_From, 0, 0])
            Time_To = utime.mktime([2020, 1, 1, 0, H_To, M_To , 0, 0])
            Difference = (Time_To - Time_From)*60*1000
            print("Difference Counted: "+str(Difference))
            return Difference

        import utime
        import machine
        import bitmapfont
        Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")

        # Actual Time:
        rtc = machine.RTC()
        Time_Act = rtc.datetime()
        Z1_Time_From = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z1_T_From_H, Z1_T_From_M, 0, 0])
        Z1_Time_To = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z1_T_To_H, Z1_T_To_M , 0, 0])
    
        Z2_Time_From = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z2_T_From_H, Z2_T_From_M, 0, 0])
        Z2_Time_To = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z2_T_To_H, Z2_T_To_M , 0, 0])

        Z3_Time_From = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z3_T_From_H, Z3_T_From_M, 0, 0])
        Z3_Time_To = utime.mktime([Time_Act[0], Time_Act[1], Time_Act[2], Time_Act[3], Z3_T_To_H, Z3_T_To_M , 0, 0])
        Time_Act = utime.mktime(rtc.datetime())

        # Difference within each Zone:
        Z1_Differnece = Time_dif(Z1_T_From_H, Z1_T_From_M, Z1_T_To_H, Z1_T_To_M)
        Z1_SCHED_TIME = round(Z1_Differnece / Z1_Cerpadlo_Count)    # [mili-seconds]

        Z2_Differnece = Time_dif(Z2_T_From_H, Z2_T_From_M, Z2_T_To_H, Z2_T_To_M)
        Z2_SCHED_TIME = round(Z2_Differnece / Z2_Cerpadlo_Count)    # [mili-seconds]

        Z3_Differnece = Time_dif(Z3_T_From_H, Z3_T_From_M, Z3_T_To_H, Z3_T_To_M)
        Z3_SCHED_TIME = round(Z3_Differnece / Z3_Cerpadlo_Count)    # [mili-seconds]

        if (Time_Act>Z1_Time_From) and (Time_Act<Z1_Time_To):
            Cerpadlo = machine.Pin(4, machine.Pin.OUT)
            Cerpadlo.on()
            print("Morning - ON")
            utime.sleep(Z1_Cerpadlo_Process)
            print("Morning - Off")
            Cerpadlo.off()

        if (Time_Act>Z2_Time_From) and (Time_Act<Z2_Time_To):
            Cerpadlo = machine.Pin(4, machine.Pin.OUT)
            Cerpadlo.on()
            print("Day - ON")
            utime.sleep(Z2_Cerpadlo_Process)
            print("Day - Off")
            Cerpadlo.off()

        if (Time_Act>Z3_Time_From) and (Time_Act<Z3_Time_To):
            Cerpadlo = machine.Pin(4, machine.Pin.OUT)
            Cerpadlo.on()
            print("Evening - ON")
            utime.sleep(Z3_Cerpadlo_Process)
            print("Evening - Off")
            Cerpadlo.off()

        # Filter
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
        
        Page = int(DB_SET[str(30)].decode('utf-8'))

    DB_SET.close()
    f_SET.close()