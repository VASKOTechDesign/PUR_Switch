def _1_Home_Page(display):
    #Setup
    import bitmapfont
    import gc
    import btree
    import Dra_Icon
    import gfx

    Grafic = gfx.GFX(240, 320, display.pixel)
    Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")

    #Background color
    display.fill(0xdedb)
    display.hline( 0, 260, 240, 0x0000)
    display.vline( 180, 260, 60, 0x0000)
    display.vline( 120, 260, 60, 0x0000)
    display.vline( 60, 260, 60, 0x0000)
    display.hline( 0, 150, 10, 0x0000)
    display.vline( 10, 0, 260, 0x0000)
    display.vline( 86, 0, 260, 0x0000)
    display.vline( 162, 0, 260, 0x0000)
    

    Font1.init()
    Font1.text("Morning", 180, 5, 0, 1)
    Font1.text("Day", 115, 5, 0, 1)
    Font1.text("Evening", 25, 5, 0, 1)
    Font1.text("Ready", 1, 1, 1, 1)
    Font1.deinit()

    #/-----------------------------Read from Settings-----------------------------/#
    f_SET = open("Database/Settings.db", "r+b")
    DB_SET = btree.open(f_SET)

    Z1_T_From_H = int(DB_SET[str(0)].decode('utf-8'))
    Z1_T_From_M = int(DB_SET[str(1)].decode('utf-8'))
    Z1_T_To_H = int(DB_SET[str(2)].decode('utf-8'))
    Z1_T_To_M = int(DB_SET[str(3)].decode('utf-8'))
    Z1_Interval = int(DB_SET[str(4)].decode('utf-8'))
    Z1_Process = int(DB_SET[str(5)].decode('utf-8'))

    Z2_T_From_H = int(DB_SET[str(6)].decode('utf-8'))
    Z2_T_From_M = int(DB_SET[str(7)].decode('utf-8'))
    Z2_T_To_H = int(DB_SET[str(8)].decode('utf-8'))
    Z2_T_To_M = int(DB_SET[str(9)].decode('utf-8'))
    Z2_Interval = int(DB_SET[str(10)].decode('utf-8'))
    Z2_Process = int(DB_SET[str(11)].decode('utf-8'))

    Z3_T_From_H = int(DB_SET[str(12)].decode('utf-8'))
    Z3_T_From_M = int(DB_SET[str(13)].decode('utf-8'))
    Z3_T_To_H = int(DB_SET[str(14)].decode('utf-8'))
    Z3_T_To_M = int(DB_SET[str(15)].decode('utf-8'))
    Z3_Interval = int(DB_SET[str(16)].decode('utf-8'))
    Z3_Process = int(DB_SET[str(17)].decode('utf-8'))

    Sched_Set = int(DB_SET[str(18)].decode('utf-8'))

    RTC_Set = int(DB_SET[str(27)].decode('utf-8'))

    DB_Init = int(DB_SET[str(62)].decode('utf-8'))

    DB_SET.close()
    f_SET.close()

    #/--------------------------Main information--------------------------/#
    #/--------------------------Zone1 . morning--------------------------/#
    #Plus buttons 
    display.fill_rectangle(202, 20, 30, 50, 0xFFFF)
    Grafic.rect(202, 20, 30, 50, 0x0000)

    display.fill_rectangle(202, 115, 30, 50, 0xFFFF)
    Grafic.rect(202, 115, 30, 50, 0x0000)

    display.fill_rectangle(202, 167, 30, 50, 0xFFFF)
    Grafic.rect(202, 167, 30, 50, 0x0000)

    display.fill_rectangle(169, 167, 30, 50, 0xFFFF)
    Grafic.rect(169, 167, 30, 50, 0x0000)

    with open('/Icons/_Plus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()
    Dra_Icon.Dra_Icon(0xB, 0x6, 39, 213, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 134, 213, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 186, 213, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 186, 180, _Icon, 0x0000, display)

    #Minus buttons
    display.fill_rectangle(169, 20, 30, 50, 0xFFFF)
    Grafic.rect(169, 20, 30, 50, 0x0000)

    display.fill_rectangle(169, 115, 30, 50, 0xFFFF)
    Grafic.rect(169, 115, 30, 50, 0x0000)

    with open('/Icons/_Minus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()
    Dra_Icon.Dra_Icon(0xB, 0x6, 39, 180, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 134, 180, _Icon, 0x0000, display)

    Font1.init()
    Font1.text("From:", 80, 220, 1, 1)
    Font1.text(str(Z1_T_From_H)+":"+str(Z1_T_From_M), 80, 210, 1, 1)

    Font1.text("To:", 80, 190, 1, 1)
    Font1.text(str(Z1_T_To_H)+":"+str(Z1_T_To_M), 80, 180, 1, 1)

    Font1.text("count:", 220, 220, 1, 1)
    Font1.text(str(Z1_Interval), 220, 210, 1, 1)

    Font1.text("Proc.:", 220, 190, 1, 1)
    Font1.text(str(Z1_Process), 220, 180, 1, 1)
    Font1.deinit()

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

    #/--------------------------Zone2 - Day--------------------------/#
    #Plus buttons 
    display.fill_rectangle(126, 20, 30, 50, 0xFFFF)
    Grafic.rect(126, 20, 30, 50, 0x0000)

    display.fill_rectangle(126, 115, 30, 50, 0xFFFF)
    Grafic.rect(126, 115, 30, 50, 0x0000)

    display.fill_rectangle(126, 167, 30, 50, 0xFFFF)
    Grafic.rect(126, 167, 30, 50, 0x0000)

    display.fill_rectangle(93, 167, 30, 50, 0xFFFF)
    Grafic.rect(93, 167, 30, 50, 0x0000)

    with open('/Icons/_Plus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()
    Dra_Icon.Dra_Icon(0xB, 0x6, 39, 137, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 134, 137, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 186, 137, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 186, 104, _Icon, 0x0000, display)

    #Minus buttons
    display.fill_rectangle(93, 20, 30, 50, 0xFFFF)
    Grafic.rect(93, 20, 30, 50, 0x0000)

    display.fill_rectangle(93, 115, 30, 50, 0xFFFF)
    Grafic.rect(93, 115, 30, 50, 0x0000)

    with open('/Icons/_Minus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()
    Dra_Icon.Dra_Icon(0xB, 0x6, 39, 104, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 134, 104, _Icon, 0x0000, display)

    Font1.init()
    Font1.text("From:", 80, 144, 1, 1)
    Font1.text(str(Z2_T_From_H)+":"+str(Z2_T_From_M), 80, 134, 1, 1)

    Font1.text("To:", 80, 114, 1, 1)
    Font1.text(str(Z2_T_To_H)+":"+str(Z2_T_To_M), 80, 104, 1, 1)

    Font1.text("Count:", 220, 144, 1, 1)
    Font1.text(str(Z2_Interval), 220, 134, 1, 1)

    Font1.text("Proc.:", 220, 114, 1, 1)
    Font1.text(str(Z2_Process), 220, 104, 1, 1)
    Font1.deinit()

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

    #/--------------------------Zone3 - Evening--------------------------/#
    #Plus buttons 
    display.fill_rectangle(50, 20, 30, 50, 0xFFFF)
    Grafic.rect(50, 20, 30, 50, 0x0000)

    display.fill_rectangle(50, 115, 30, 50, 0xFFFF)
    Grafic.rect(50, 115, 30, 50, 0x0000)

    display.fill_rectangle(50, 167, 30, 50, 0xFFFF)
    Grafic.rect(50, 167, 30, 50, 0x0000)

    display.fill_rectangle(17, 167, 30, 50, 0xFFFF)
    Grafic.rect(17, 167, 30, 50, 0x0000)

    with open('/Icons/_Plus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()
    Dra_Icon.Dra_Icon(0xB, 0x6, 39, 61, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 134, 61, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 186, 61, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 186, 28, _Icon, 0x0000, display)

    #Minus buttons
    display.fill_rectangle(17, 20, 30, 50, 0xFFFF)
    Grafic.rect(17, 20, 30, 50, 0x0000)

    display.fill_rectangle(17, 115, 30, 50, 0xFFFF)
    Grafic.rect(17, 115, 30, 50, 0x0000)

    with open('/Icons/_Minus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()
    Dra_Icon.Dra_Icon(0xB, 0x6, 39, 28, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 134, 28, _Icon, 0x0000, display)

    Font1.init()
    Font1.text("From:", 80, 68, 1, 1)
    Font1.text(str(Z3_T_From_H)+":"+str(Z3_T_From_M), 80, 58, 1, 1)

    Font1.text("To:", 80, 38, 1, 1)
    Font1.text(str(Z3_T_To_H)+":"+str(Z3_T_To_M), 80, 28, 1, 1)

    Font1.text("Count:", 220, 68, 1, 1)
    Font1.text(str(Z3_Interval), 220, 58, 1, 1)

    Font1.text("Proc.:", 220, 38, 1, 1)
    Font1.text(str(Z3_Process), 220, 28, 1, 1)
    Font1.deinit()

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())


    #/-----------------------------Sleep Button-----------------------------/#
    #Icon:
    with open('/Icons/_Sleep_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()

    Dra_Icon.Dra_Icon(0x22, 0x22, 0x112, 0xC1, _Icon, 0x0000, display)

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

    #/------------------------------Manual / Filter------------------------------/#    
    Font1.init()
    Font1.text("Filtr/", 275, 149, 1, 1)
    Font1.text("Manual", 275, 139, 1, 1)
    Font1.deinit()

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

    #/-------------------------------RTC Set-------------------------------/#
    #Icon:
    with open('/Icons/_RTC_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()

    Dra_Icon.Dra_Icon(0x38, 0x20, 0x106, 0x4A, _Icon, 0x0000, display)

    if RTC_Set == 1:
        display.fill_rectangle(116, 261, 4, 59, 0x7fc0)
    else:
        display.fill_rectangle(116, 261, 4, 59, 0xf800)

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())


    #/-----------------------------OK Buttons-----------------------------/#
    #Icon:
    with open('/Icons/_OK_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()

    Dra_Icon.Dra_Icon(0x1A, 0x16, 0x118, 0x13, _Icon, 0x0000, display)

    if Sched_Set == 1:
        display.fill_rectangle(56, 261, 4, 59, 0x7fc0)
    else:
        display.fill_rectangle(56, 261, 4, 59, 0xf800)

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())