def _3_Manual(display,DB_SET):
    #Setup
    import bitmapfont
    import btree
    import gfx
    import gc
    import Dra_Icon

    Grafic = gfx.GFX(240, 320, display.pixel)
    Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")

    #Background color
    display.fill(0xa554)


    #/-----------------------------Read from Settings-----------------------------/#
    f_SET = open("Database/Settings.db", "r+b")
    DB_SET = btree.open(f_SET)

    Filtr_Count = int(DB_SET[str(40)].decode('utf-8'))
    Filtr_Interval = int(DB_SET[str(41)].decode('utf-8'))

    DB_SET.close()
    f_SET.close()

    #/-----------------------------Cerpadlo-----------------------------/#
    #Manual On Buttons
    Font1.init()
    Font1.text("Cerpadlo", 33, 180, 1, 1)
    display.fill_rectangle(100, 10, 75, 100, 0xFFFF)
    Grafic.rect(100, 10, 75, 100, 0x0000)
    Font1.text("Manual ON", 33, 135, 1, 1)

    #Manual Off Buttons
    display.fill_rectangle(10, 10, 75, 100, 0xFFFF)
    display.fill_rectangle(80, 11, 4, 98, 0xf800) # Status
    Grafic.rect(10, 10, 75, 100, 0x0000)
    Font1.text("Manual Off", 30, 40, 1, 1)
    Font1.deinit()

    display.hline( 0, 124, 200, 0x0000)

    #/-----------------------------Filter-----------------------------/#
    #Manual On Buttons
    Font1.init()
    Font1.text("Filtr", 175, 180, 1, 1)
    display.fill_rectangle(100, 140, 75, 100, 0xFFFF)
    Grafic.rect(100, 140, 75, 100, 0x0000)
    Font1.text("Manual ON", 160, 135, 1, 1)

    #Manual Off Buttons
    display.fill_rectangle(10, 140, 75, 100, 0xFFFF)
    display.fill_rectangle(80, 141, 4, 98, 0xf800) # Status
    Grafic.rect(10, 140, 75, 100, 0x0000)
    Font1.text("Manual OFF", 157, 40, 1, 1)
    Font1.deinit()

    # Day Interval and per/Day
    Font1.init()
    Font1.text("Per/Day", 258, 167, 1, 1)
    Font1.text(str(Filtr_Count), 275, 157, 1, 1)
    Font1.text("Interval", 255, 75, 1, 1)
    Font1.text(str(Filtr_Interval), 275, 65, 1, 1)

    display.fill_rectangle(120, 255, 30, 50, 0xFFFF)
    Grafic.rect(120, 255, 30, 50, 0x0000)

    display.fill_rectangle(30, 255, 30, 50, 0xFFFF)
    Grafic.rect(30, 255, 30, 50, 0x0000)

    with open('/Icons/_Plus_Icon.bin', 'rb') as f:
        _Icon = list(f.read())

    Dra_Icon.Dra_Icon(0xB, 0x6, 275, 132, _Icon, 0x0000, display)
    Dra_Icon.Dra_Icon(0xB, 0x6, 275, 42, _Icon, 0x0000, display)

    #/-----------------------------Back Buttons-----------------------------/#
    display.fill_rectangle(190, 270, 50, 50, 0xFFFF)
    Grafic.rect(190, 270, 50, 50, 0x0000)

    #Icon:
    with open('/Icons/_Back_Icon.bin', 'rb') as f:
        _Icon = list(f.read())
    f.close()

    Dra_Icon.Dra_Icon(0x1A, 0x18, 0x11B, 0xCB, _Icon, 0x0000, display)

    #Memory management
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
