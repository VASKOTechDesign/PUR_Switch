def _1_Find_Page(coordinates, display):
    def Write_Message(text, x, y, landscape, unknown):
        import bitmapfont
        Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")
        Font1.init()
        Font1.text(str(text), x, y, landscape, unknown)
        Font1.deinit()

    import gc

    #/-------------------------Read from Settings-------------------------/#
    import btree
    f_SET = open("Database/Settings.db", "r+b")
    DB_SET = btree.open(f_SET)
    page = int(DB_SET[str(30)].decode('utf-8'))

    #/-----------------------------Sleep Page-----------------------------/#
    if page == 0:
        #Wake up from screen save mode
        DB_SET[str(30)] = "1"
        DB_SET.flush()
        import machine
        ts_LED = machine.Pin(32, machine.Pin.OUT)
        ts_LED.on()

    #/-----------------------------Home Page-----------------------------/#
    if page == 1:
        #Sleep
        if ((300 < coordinates[0] < 1100)and(350 < coordinates[1] < 850)):
            DB_SET[str(30)] = "0"
            DB_SET.flush()
            import machine
            ts_LED = machine.Pin(32, machine.Pin.OUT)
            ts_LED.off()

        #Manual
        if ((1200 < coordinates[0] < 2100)and(350 < coordinates[1] < 850)):
            DB_SET[str(30)] = "3"
            DB_SET.flush()
            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
            import _3_Manual_mod
            _3_Manual_mod._3_Manual(display,DB_SET)

        #RTC Setup
        if ((2150 < coordinates[0] < 2950)and(350 < coordinates[1] < 850)):
            DB_SET[str(30)] = "11"
            DB_SET.flush()
            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
            import _11_Date_Time_mod
            _11_Date_Time_mod._11_Date_Time_Set(display, DB_SET)

        # Confirm Button   
        if ((3019 < coordinates[0] < 3766)and(356 < coordinates[1] < 954)):
            DB_SET[str(18)] = "1"
            DB_SET.flush()

            display.fill_rectangle(56, 261, 4, 59, 0x7fc0)

            import Scheduler
            Scheduler.Schedule_Cerpadlo(DB_SET, display)
        #-----------Morning-----------#
        # + Time_From
        if ((354 < coordinates[0] < 693)and(3181 < coordinates[1] < 3711)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(1, display, DB_SET)

        # - Time_From
        if ((836 < coordinates[0] < 1253)and(3183 < coordinates[1] < 3675)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(2, display, DB_SET)

        # + Time_To
        if ((385 < coordinates[0] < 725)and(2122 < coordinates[1] < 2638)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(3, display, DB_SET)

        # - Time_To
        if ((820 < coordinates[0] < 1227)and(2130 < coordinates[1] < 2646)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(4, display, DB_SET)

        # Interval
        if ((369 < coordinates[0] < 697)and(1539 < coordinates[1] < 2030)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(5, display, DB_SET)

        # Process time [minutes]
        if ((853 < coordinates[0] < 1211)and(1521 < coordinates[1] < 2034)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(6, display, DB_SET)

        #-----------Day-----------#
        # + Time_From
        if ((1519 < coordinates[0] < 1879)and(3199 < coordinates[1] < 3679)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(7, display, DB_SET)

        # - Time_From
        if ((2039 < coordinates[0] < 2415)and(3195 < coordinates[1] < 3679)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(8, display, DB_SET)

        # + Time_To
        if ((1507 < coordinates[0] < 1891)and(2129 < coordinates[1] < 2633)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(9, display, DB_SET)

        # - Time_To
        if ((2046 < coordinates[0] < 2427)and(2115 < coordinates[1] < 2639)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(10, display, DB_SET)

        # Interval
        if ((1514 < coordinates[0] < 1871)and(1512 < coordinates[1] < 2014)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(11, display, DB_SET)

        # Process time [minutes]
        if ((2061 < coordinates[0] < 2439)and(1521 < coordinates[1] < 2003)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(12, display, DB_SET)

        #-----------Evening-----------#
        # + Time_From
        if ((2711 < coordinates[0] < 3167)and(3174 < coordinates[1] < 3671)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(13, display, DB_SET)

        # - Time_From
        if ((3243 < coordinates[0] < 3583)and(3189 < coordinates[1] < 3671)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(14, display, DB_SET)

        # + Time_To
        if ((2727 < coordinates[0] < 3099)and(2141 < coordinates[1] < 2635)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(15, display, DB_SET)

        # - Time_To
        if ((3259 < coordinates[0] < 3593)and(2137 < coordinates[1] < 2615)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(16, display, DB_SET)

        # Interval
        if ((2749 < coordinates[0] < 3093)and(1533 < coordinates[1] < 2022)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(17, display, DB_SET)

        # Process time [minutes]
        if ((3259 < coordinates[0] < 3677)and(1527 < coordinates[1] < 2015)):
            import _1_Sched_Set
            _1_Sched_Set.Sched_Set(18, display, DB_SET)

    #/-----------------------------Manual-----------------------------/#
    if page == 3:
        #Back
        if ((230 < coordinates[0] < 930)and(350 < coordinates[1] < 850)):
            import machine
            Cerpadlo = machine.Pin(4, machine.Pin.OUT)
            Filtrace = machine.Pin(15, machine.Pin.OUT)

            Cerpadlo.off()
            Filtrace.off()

            DB_SET[str(18)] = "0"  
            DB_SET[str(30)] = "1"
            DB_SET.flush()
            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
            import _1_Home_Page_mod
            _1_Home_Page_mod._1_Home_Page(display)

        # Manual ON
        if ((1230 < coordinates[0] < 2329)and(2715 < coordinates[1] < 3775)):
            import _3_Manual_Set
            _3_Manual_Set.ON_OFF(1, display, DB_SET)

        # Manual OFF
        if ((2608 < coordinates[0] < 3707)and(2693 < coordinates[1] < 3789)):
            import _3_Manual_Set
            _3_Manual_Set.ON_OFF(2, display, DB_SET)

        # Filter ON
        if ((1199 < coordinates[0] < 2324)and(1244 < coordinates[1] < 2365)): 
            import _3_Manual_Set
            _3_Manual_Set.ON_OFF(3, display, DB_SET)

        # Filter OFF
        if ((2615 < coordinates[0] < 3706)and(1248 < coordinates[1] < 2356)):
            import _3_Manual_Set
            _3_Manual_Set.ON_OFF(4, display, DB_SET)

        # Filter Interval [/day]
        if ((1580 < coordinates[0] < 2022)and(513 < coordinates[1] < 1035)):
            import _3_Manual_Set
            _3_Manual_Set.ON_OFF(5, display, DB_SET)

        # Filter - Process Time [minutes]
        if ((3007 < coordinates[0] < 3415)and(504 < coordinates[1] < 1043)):
            import _3_Manual_Set
            _3_Manual_Set.ON_OFF(6, display, DB_SET)

    #/--------------------------Date and Time---------------------------/#
    if page == 11:
        #Back
        if ((230 < coordinates[0] < 930)and(350 < coordinates[1] < 850)):
            DB_SET[str(30)] = "1"
            DB_SET.flush()
            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
            import _1_Home_Page_mod
            _1_Home_Page_mod._1_Home_Page(display)

        #Confirm
        if ((3200 < coordinates[0] < 3800)and(350 < coordinates[1] < 850)):
            DB_SET[str(30)] = "1"
            DB_SET.flush()

            DB_SET[str(27)] = "1"
            DB_SET.flush()

            #Real Time Clock
            import machine
            rtc = machine.RTC()
            rtc.init((int(DB_SET[str(21)].decode('utf-8')), int(DB_SET[str(22)].decode('utf-8')), int(DB_SET[str(23)].decode('utf-8')), int(DB_SET[str(26)].decode('utf-8')), int(DB_SET[str(24)].decode('utf-8')), int(DB_SET[str(25)].decode('utf-8')), 0, 0))
            #Format: year, month, day, weekday, hour, minute, second, microseconds

            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
            import _1_Home_Page_mod
            _1_Home_Page_mod._1_Home_Page(display)

        #Year +
        if ((1575 < coordinates[0] < 2025)and(3230 < coordinates[1] < 3725)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(1, display, DB_SET)

        #Month +
        if ((1575 < coordinates[0] < 2025)and(2620 < coordinates[1] < 3125)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(2, display, DB_SET)

        #Day +
        if ((1575 < coordinates[0] < 2025)and(1980 < coordinates[1] < 2525)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(3, display, DB_SET)

        #Hour +
        if ((1575 < coordinates[0] < 2025)and(1170 < coordinates[1] < 1725)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(4, display, DB_SET)

        #Minute +
        if ((1575 < coordinates[0] < 2025)and(560 < coordinates[1] < 1125)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(5, display, DB_SET)

        #Year -
        if ((2555 < coordinates[0] < 2970)and(3230 < coordinates[1] < 3725)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(6, display, DB_SET)

        #Month -
        if ((2555 < coordinates[0] < 2970)and(2620 < coordinates[1] < 3125)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(7, display, DB_SET)

        #Day -
        if ((2555 < coordinates[0] < 2970)and(1980 < coordinates[1] < 2525)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(8, display, DB_SET)

        #Hour -
        if ((2555 < coordinates[0] < 2970)and(1170 < coordinates[1] < 1725)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(9, display, DB_SET)

        #Minute -
        if ((2555 < coordinates[0] < 2970)and(560 < coordinates[1] < 1125)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(10, display, DB_SET)

        #WeekDay +
        if ((3200 < coordinates[0] < 3625)and(2150 < coordinates[1] < 2700)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(11, display, DB_SET)

        #WeekDay -
        if ((3250 < coordinates[0] < 3625)and(1530 < coordinates[1] < 2050)):
            import _11_Date_Time_Update
            _11_Date_Time_Update.Date_Time_Update(12, display, DB_SET)

    DB_SET.close()
    f_SET.close()
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
