def _11_Date_Time_Set(display,DB_SET):
    #Setup
    import bitmapfont
    import gfx
    import gc
    import Dra_Icon

    Grafic = gfx.GFX(240, 320, display.pixel)
    Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")

    #Background color
    display.fill(0xa554)

    #/-----------------------------Back Buttons-----------------------------/#
    display.fill_rectangle(190, 270, 50, 50, 0xFFFF)
    Grafic.rect(190, 270, 50, 50,0x0000)

    #Icon:
    with open('/Icons/_Back_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()

    Dra_Icon.Dra_Icon(0x1A, 0x18, 0x11B, 0xCB, _Icon, 0x0000, display)

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

    #/-----------------------------OK Buttons-----------------------------/#
    display.fill_rectangle(0, 270, 50, 50, 0xFFFF)
    Grafic.rect(0, 270, 50, 50, 0x0000)

    #Icon:
    with open('/Icons/_OK_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()

    Dra_Icon.Dra_Icon(0x1A, 0x16, 0x11B, 0xD, _Icon, 0x0000, display)

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

    #/--------------------------Date and Time Area--------------------------/#
    Grafic.rect(55, 10, 130, 170, 0x0000)
    Grafic.rect(55, 190, 130, 120, 0x0000)
    Grafic.rect(10, 10, 40, 210, 0x0000)

    Font1.init()
    Font1.text("Set actual date and time used by system:", 10, 190, 1, 1)
    Font1.text("Date:", 20, 170, 1, 1)
    Font1.text("Time:", 200, 170, 1, 1)
    Font1.text("Week-day:", 20, 35, 1, 1)

    Font1.text("Year", 29, 155, 1, 1)
    Font1.text("Month", 82, 155, 1, 1)
    Font1.text("Day", 141, 155, 1, 1)
    Font1.text("Hour", 209, 155, 1, 1)
    Font1.text("Minute", 258, 155, 1, 1)
    Font1.deinit()

    #Plus buttons 
    display.fill_rectangle(120, 15, 30, 50, 0xFFFF)
    Grafic.rect(120, 15, 30, 50, 0x0000)

    display.fill_rectangle(120, 70, 30, 50, 0xFFFF)
    Grafic.rect(120, 70, 30, 50, 0x0000)

    display.fill_rectangle(120, 125, 30, 50, 0xFFFF)
    Grafic.rect(120, 125, 30, 50, 0x0000)

    display.fill_rectangle(120, 195, 30, 50, 0xFFFF)
    Grafic.rect(120, 195, 30, 50, 0x0000)

    display.fill_rectangle(120, 250, 30, 50, 0xFFFF)
    Grafic.rect(120, 250, 30, 50, 0x0000)

    display.fill_rectangle(15, 110, 30, 50, 0xFFFF)
    Grafic.rect(15, 110, 30, 50, 0x0000)

    #Plus Icon
    with open('/Icons/_Plus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()

    Dra_Icon.Dra_Icon(0xB, 0x6, 0x23, 0x84, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0x5A, 0x84, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0x91, 0x84, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0xD7, 0x84, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0x10E, 0x84, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0x82, 0x1B, _Icon, 0x0000, display)

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

    #Minus buttons
    display.fill_rectangle(60, 15, 30, 50, 0xFFFF)
    Grafic.rect(60, 15, 30, 50, 0x0000)

    display.fill_rectangle(60, 70, 30, 50, 0xFFFF)
    Grafic.rect(60, 70, 30, 50, 0x0000)

    display.fill_rectangle(60, 125, 30, 50, 0xFFFF)
    Grafic.rect(60, 125, 30, 50, 0x0000)

    display.fill_rectangle(60, 195, 30, 50, 0xFFFF)
    Grafic.rect(60, 195, 30, 50, 0x0000)

    display.fill_rectangle(60, 250, 30, 50, 0xFFFF)
    Grafic.rect(60, 250, 30, 50, 0x0000)

    display.fill_rectangle(15, 165, 30, 50, 0xFFFF)
    Grafic.rect(15, 165, 30, 50, 0x0000)

    #Minus Icon
    with open('/Icons/_Minus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()

    Dra_Icon.Dra_Icon(0xB, 0x6, 0x23, 0x46, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0x5A, 0x46, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0x91, 0x46, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0xD7, 0x46, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0x10E, 0x46, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 0xB9, 0x1B, _Icon, 0x0000, display)

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

    #/------------------------Data from DB------------------------/#
    Rec_Year = DB_SET[str(21)].decode('utf-8')
    Rec_Month = DB_SET[str(22)].decode('utf-8')
    Rec_Day = DB_SET[str(23)].decode('utf-8')
    Rec_Hour = DB_SET[str(24)].decode('utf-8')
    Rec_Minute = DB_SET[str(25)].decode('utf-8')
    Rec_WeekDay = int(DB_SET[str(26)].decode('utf-8'))

    Font1.init()
    Font1.text(str(Rec_Year), 27, 100, 1, 1)
    Font1.text(str(Rec_Month), 90, 100, 1, 1)
    Font1.text(str(Rec_Day), 145, 100, 1, 1)
    Font1.text(str(Rec_Hour), 215, 100, 1, 1)
    Font1.text(str(Rec_Minute), 270, 100, 1, 1)

    if Rec_WeekDay == 0:
        Font1.text("Monday", 30, 20, 1, 1)

    if Rec_WeekDay == 1:
        Font1.text("Tuesday", 30, 20, 1, 1)

    if Rec_WeekDay == 2:
        Font1.text("Wednesday", 30, 20, 1, 1)

    if Rec_WeekDay == 3:
        Font1.text("Thursday", 30, 20, 1, 1)

    if Rec_WeekDay == 4:
        Font1.text("Friday", 30, 20, 1, 1)

    if Rec_WeekDay == 5:
        Font1.text("Saturday", 30, 20, 1, 1)

    if Rec_WeekDay == 6:
        Font1.text("Sunday", 30, 20, 1, 1)

    Font1.deinit()
