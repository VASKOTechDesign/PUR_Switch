def Date_Time_Update(Button,display,DB_SET):
    #Setup
    import bitmapfont
    Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")
    Font1.init()

    #Plus Buttons - limit numbers to maximum
    if Button==1:
        RTC_Year = int(DB_SET[str(21)].decode('utf-8'))
        display.fill_rectangle(98, 25, 15, 30, 0xa554)
        Font1.text(str(RTC_Year + 1), 27, 100, 1, 1)
        DB_SET[str(21)] = str(RTC_Year + 1) 

    if Button==2:
        RTC_Month = int(DB_SET[str(22)].decode('utf-8'))
        display.fill_rectangle(98, 88, 15, 15, 0xa554)
        if RTC_Month<9:
            Font1.text("0"+str(RTC_Month + 1), 90, 100, 1, 1)
            DB_SET[str(22)] = "0"+str(RTC_Month + 1) 
        if (RTC_Month==9 or RTC_Month==10 or RTC_Month==11):
            Font1.text(str(RTC_Month + 1), 90, 100, 1, 1)
            DB_SET[str(22)] = str(RTC_Month + 1) 
        if RTC_Month==12:
            Font1.text("12", 90, 100, 1, 1)
            DB_SET[str(22)] = "12"

    if Button==3:
        RTC_Day = int(DB_SET[str(23)].decode('utf-8'))
        display.fill_rectangle(98, 143, 15, 15, 0xa554)
        if RTC_Day<9:
            Font1.text("0"+str(RTC_Day + 1), 145, 100, 1, 1)
            DB_SET[str(23)] = "0"+str(RTC_Day + 1) 
        if (RTC_Day>8 and RTC_Day<30):
            Font1.text(str(RTC_Day + 1), 145, 100, 1, 1)
            DB_SET[str(23)] = str(RTC_Day + 1) 
        if RTC_Day>29:
            Font1.text("31", 145, 100, 1, 1)
            DB_SET[str(23)] = "31"

    if Button==4:
        RTC_Hour = int(DB_SET[str(24)].decode('utf-8'))
        display.fill_rectangle(98, 213, 15, 15, 0xa554)
        if RTC_Hour<9:
            Font1.text("0"+str(RTC_Hour + 1), 215, 100, 1, 1)
            DB_SET[str(24)] = "0"+str(RTC_Hour + 1) 
        if (RTC_Hour>8 and RTC_Hour<22):
            Font1.text(str(RTC_Hour + 1), 215, 100, 1, 1)
            DB_SET[str(24)] = str(RTC_Hour + 1) 
        if RTC_Hour>21:
            Font1.text("23", 215, 100, 1, 1)
            DB_SET[str(24)] = "23"

    if Button==5:
        RTC_Minute = int(DB_SET[str(25)].decode('utf-8'))
        display.fill_rectangle(98, 268, 15, 15, 0xa554)
        if RTC_Minute<9:
            Font1.text("0"+str(RTC_Minute + 1), 270, 100, 1, 1)
            DB_SET[str(25)] = "0"+str(RTC_Minute + 1) 
        if (RTC_Minute>8 and RTC_Minute<58):
            Font1.text(str(RTC_Minute + 1), 270, 100, 1, 1)
            DB_SET[str(25)] = str(RTC_Minute + 1) 
        if RTC_Minute>57:
            Font1.text("59", 270, 100, 1, 1)
            DB_SET[str(25)] = "59"

    #Minus Buttons - limit numbers to minum
    if Button==6:
        RTC_Year = int(DB_SET[str(21)].decode('utf-8'))
        display.fill_rectangle(98, 25, 15, 30, 0xa554)
        Font1.text(str(RTC_Year - 1), 27, 100, 1, 1)
        DB_SET[str(21)] = str(RTC_Year - 1) 

    if Button==7:
        RTC_Month = int(DB_SET[str(22)].decode('utf-8'))
        display.fill_rectangle(98, 88, 15, 15, 0xa554)
        if RTC_Month>10:
            Font1.text(str(RTC_Month - 1), 90, 100, 1, 1)
            DB_SET[str(22)] = str(RTC_Month - 1) 
        if (RTC_Month>1 and RTC_Month<11):
            Font1.text("0"+str(RTC_Month - 1), 90, 100, 1, 1)
            DB_SET[str(22)] = "0"+str(RTC_Month - 1) 
        if RTC_Month==1:
            Font1.text("01", 90, 100, 1, 1)
            DB_SET[str(22)] = "01"

    if Button==8:
        RTC_Day = int(DB_SET[str(23)].decode('utf-8'))
        display.fill_rectangle(98, 143, 15, 15, 0xa554)
        if RTC_Day>10:
            Font1.text(str(RTC_Day - 1), 145, 100, 1, 1)
            DB_SET[str(23)] = str(RTC_Day - 1) 
        if (RTC_Day>1 and RTC_Day<11):
            Font1.text("0"+str(RTC_Day - 1), 145, 100, 1, 1)
            DB_SET[str(23)] = "0"+str(RTC_Day - 1) 
        if RTC_Day==1:
            Font1.text("01", 145, 100, 1, 1)
            DB_SET[str(23)] = "01"

    if Button==9:
        RTC_Hour = int(DB_SET[str(24)].decode('utf-8'))
        display.fill_rectangle(98, 213, 15, 15, 0xa554)
        if RTC_Hour>10:
            Font1.text(str(RTC_Hour - 1), 215, 100, 1, 1)
            DB_SET[str(24)] = str(RTC_Hour - 1) 
        if (RTC_Hour>0 and RTC_Hour<11):
            Font1.text("0"+str(RTC_Hour - 1), 215, 100, 1, 1)
            DB_SET[str(24)] = "0"+str(RTC_Hour - 1)
        if RTC_Hour==0:
            Font1.text("00", 215, 100, 1, 1)
            DB_SET[str(24)] = "00"

    if Button==10:
        RTC_Minute = int(DB_SET[str(25)].decode('utf-8'))
        display.fill_rectangle(98, 268, 15, 15, 0xa554)
        if RTC_Minute>10:
            Font1.text(str(RTC_Minute - 1), 270, 100, 1, 1)
            DB_SET[str(25)] = str(RTC_Minute - 1) 
        if (RTC_Minute>0 and RTC_Minute<11):
            Font1.text("0"+str(RTC_Minute - 1), 270, 100, 1, 1)
            DB_SET[str(25)] = "0"+str(RTC_Minute - 1) 
        if RTC_Minute==0:
            Font1.text("00", 270, 100, 1, 1)
            DB_SET[str(25)] = "00"

    if Button==11:
        RTC_WeekDay = int(DB_SET[str(26)].decode('utf-8'))
        display.fill_rectangle(18, 28, 15, 70, 0xa554)
        if RTC_WeekDay == 6:
            DB_SET[str(26)] = str(RTC_WeekDay) 
            RTC_WeekDay = RTC_WeekDay
        else:
            DB_SET[str(26)] = str(RTC_WeekDay + 1) 
            RTC_WeekDay = RTC_WeekDay + 1        
        if RTC_WeekDay==1:
            Font1.text("Tuesday", 30, 20, 1, 1)
        if RTC_WeekDay==2:
            Font1.text("Wednesday", 30, 20, 1, 1)
        if RTC_WeekDay==3:
            Font1.text("Thursday", 30, 20, 1, 1)
        if RTC_WeekDay==4:
            Font1.text("Friday", 30, 20, 1, 1)
        if RTC_WeekDay==5:
            Font1.text("Satruday", 30, 20, 1, 1)
        if RTC_WeekDay==6:
            Font1.text("Sunday", 30, 20, 1, 1)      

    if Button==12:
        RTC_WeekDay = int(DB_SET[str(26)].decode('utf-8'))
        display.fill_rectangle(18, 28, 15, 70, 0xa554)
        if RTC_WeekDay == 0:
            DB_SET[str(26)] = str(RTC_WeekDay) 
            RTC_WeekDay = RTC_WeekDay
        else:
            DB_SET[str(26)] = str(RTC_WeekDay - 1) 
            RTC_WeekDay = RTC_WeekDay - 1        
        if RTC_WeekDay==0:
            Font1.text("Monday", 30, 20, 1, 1)
        if RTC_WeekDay==1:
            Font1.text("Tuesday", 30, 20, 1, 1)
        if RTC_WeekDay==2:
            Font1.text("Wednesday", 30, 20, 1, 1)
        if RTC_WeekDay==3:
            Font1.text("Thursday", 30, 20, 1, 1)
        if RTC_WeekDay==4:
            Font1.text("Friday", 30, 20, 1, 1)
        if RTC_WeekDay==5:
            Font1.text("Satruday", 30, 20, 1, 1)    

    Font1.deinit()
