def ON_OFF(Button, display, DB_SET):
    #Setup
    import bitmapfont
    import machine
    Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")
    Font1.init()
    Cerpadlo = machine.Pin(4, machine.Pin.OUT)
    Filtrace = machine.Pin(15, machine.Pin.OUT)

    if Button==1:
        Cerpadlo.on()
        display.fill_rectangle(170, 11, 4, 98, 0x7fc0) # Status - ON
        display.fill_rectangle(80, 11, 4, 98, 0xFFFF) # Status - hide OFF

    if Button==2:
        Cerpadlo.off()
        display.fill_rectangle(170, 11, 4, 98, 0xFFFF) # Status - hide ON
        display.fill_rectangle(80, 11, 4, 98, 0xf800) # Status - OFF

    if Button==3:
        Filtrace.on()
        display.fill_rectangle(170, 141, 4, 98, 0x7fc0) # Status - ON
        display.fill_rectangle(80, 141, 4, 98, 0xFFFF) # Status - hide OFF

    if Button==4:
        Filtrace.off()
        display.fill_rectangle(170, 141, 4, 98, 0xFFFF) # Status - hide ON
        display.fill_rectangle(80, 141, 4, 98, 0xf800) # Status - OFF

    if Button==5:
        Filtr_Count = int(DB_SET[str(40)].decode('utf-8'))
        if Filtr_Count >= 59:
            DB_SET[str(40)] = "00" 
            Filtr_Count = "00"
        else:
            DB_SET[str(40)] = str(Filtr_Count + 1) 
            Filtr_Count += 1
        DB_SET.flush()   

        # Print to display new time
        display.fill_rectangle(156, 274, 10, 25, 0xa554)
        Font1.text(str(Filtr_Count), 275, 157, 1, 1)

    if Button==6:
        Filtr_Interval = int(DB_SET[str(41)].decode('utf-8'))
        if Filtr_Interval >= 59:
            DB_SET[str(41)] = "00" 
            Filtr_Interval = "00"
        else:
            DB_SET[str(41)] = str(Filtr_Interval + 1) 
            Filtr_Interval += 1
        DB_SET.flush()  

        # Print to display new time
        display.fill_rectangle(64, 274, 10, 25, 0xa554)
        Font1.text(str(Filtr_Interval), 275, 65, 1, 1)

    Font1.deinit()