def Sched_Set(Button, display, DB_SET):
    #Setup
    import bitmapfont
    Font1 = bitmapfont.BitmapFont(240, 320, display.pixel, font_name="font5x8.bin")
    Font1.init()

    display.fill_rectangle(56, 261, 4, 59, 0xf800)
    DB_SET[str(18)] = "0"
    DB_SET.flush()

    def Time_Counter_Plus(Hodina, Minuta, DB_H, DB_M):
        if Minuta == 50:
            DB_SET[str(DB_H)] = str(Hodina + 1) 
            DB_SET[str(DB_M)] = "00" 
            Hodina += 1
            Minuta = "00"
        else:
            DB_SET[str(DB_M)] = str(Minuta + 10)
            Minuta += 10
        DB_SET.flush()
        return Hodina, Minuta

    def Time_Counter_Minus(Hodina, Minuta, DB_H, DB_M):
        if Minuta == 0:
            DB_SET[str(DB_H)] = str(Hodina - 1) 
            DB_SET[str(DB_M)] = "50" 
            Hodina -= 1
            Minuta = "50"
        else:
            DB_SET[str(DB_M)] = str(Minuta - 10)
            Minuta -= 10
        DB_SET.flush()
        return Hodina, Minuta

    def Counter_Plus(Counter, DB_Int):
        if Counter == 119:
            DB_SET[str(DB_Int)] = "00" 
            Counter = "00"
        else:
            DB_SET[str(DB_Int)] = str(Counter + 1)
            Counter += 1
        DB_SET.flush()
        return Counter

    def Process_Plus(Process_T, DB_Proc):
        if Process_T == 59:
            DB_SET[str(DB_Proc)] = "00" 
            Process_T = "00"
        else:
            DB_SET[str(DB_Proc)] = str(Process_T + 1)
            Process_T += 1
        DB_SET.flush()
        return Process_T

    #--------------Morning--------------#
    # + Time From
    if Button==1:
        Z1_T_From_H = int(DB_SET[str(0)].decode('utf-8'))
        Z1_T_From_M = int(DB_SET[str(1)].decode('utf-8'))
        Z1_T_From_H, Z1_T_From_M = Time_Counter_Plus(Z1_T_From_H, Z1_T_From_M, 0, 1)
        
        # Print to display new time
        display.fill_rectangle(209, 79, 10, 32, 0xdedb)
        Font1.text(str(Z1_T_From_H)+":"+str(Z1_T_From_M), 80, 210, 1, 1)

    # - Time From
    if Button==2:
        Z1_T_From_H = int(DB_SET[str(0)].decode('utf-8'))
        Z1_T_From_M = int(DB_SET[str(1)].decode('utf-8'))
        Z1_T_From_H, Z1_T_From_M = Time_Counter_Minus(Z1_T_From_H, Z1_T_From_M, 0, 1)

        # Print to display new time
        display.fill_rectangle(209, 79, 10, 32, 0xdedb)
        Font1.text(str(Z1_T_From_H)+":"+str(Z1_T_From_M), 80, 210, 1, 1)

    # + Time To
    if Button==3:
        Z1_T_To_H = int(DB_SET[str(2)].decode('utf-8'))
        Z1_T_To_M = int(DB_SET[str(3)].decode('utf-8'))
        Z1_T_To_H, Z1_T_To_M = Time_Counter_Plus(Z1_T_To_H, Z1_T_To_M, 2, 3)
        
        # Print to display new time
        display.fill_rectangle(179, 79, 10, 32, 0xdedb)
        Font1.text(str(Z1_T_To_H)+":"+str(Z1_T_To_M), 80, 180, 1, 1)

    # - Time From
    if Button==4:
        Z1_T_To_H = int(DB_SET[str(2)].decode('utf-8'))
        Z1_T_To_M = int(DB_SET[str(3)].decode('utf-8'))
        Z1_T_To_H, Z1_T_To_M = Time_Counter_Minus(Z1_T_To_H, Z1_T_To_M, 2, 3)
        
        # Print to display new time
        display.fill_rectangle(179, 79, 10, 32, 0xdedb)
        Font1.text(str(Z1_T_To_H)+":"+str(Z1_T_To_M), 80, 180, 1, 1)

    # Counter [counts]
    if Button==5:
        Z1_Counter = int(DB_SET[str(4)].decode('utf-8'))
        Z1_Counter = Counter_Plus(Z1_Counter, 4)

        # Print to display new time
        display.fill_rectangle(209, 219, 10, 20, 0xdedb)
        Font1.text(str(Z1_Counter), 220, 210, 1, 1)

    # Process time [minutes]
    if Button==6:
        Z1_Process = int(DB_SET[str(5)].decode('utf-8'))
        Z1_Process = Process_Plus(Z1_Process, 5)

        # Print to display new time
        display.fill_rectangle(179, 219, 10, 15, 0xdedb)
        Font1.text(str(Z1_Process), 220, 180, 1, 1)


    #--------------Day--------------#
    # + Time From
    if Button==7:
        Z2_T_From_H = int(DB_SET[str(6)].decode('utf-8'))
        Z2_T_From_M = int(DB_SET[str(7)].decode('utf-8'))
        Z2_T_From_H, Z2_T_From_M = Time_Counter_Plus(Z2_T_From_H, Z2_T_From_M, 6, 7)
        
        # Print to display new time
        display.fill_rectangle(133, 79, 10, 32, 0xdedb)
        Font1.text(str(Z2_T_From_H)+":"+str(Z2_T_From_M), 80, 134, 1, 1)

    # - Time From
    if Button==8:
        Z2_T_From_H = int(DB_SET[str(6)].decode('utf-8'))
        Z2_T_From_M = int(DB_SET[str(7)].decode('utf-8'))
        Z2_T_From_H, Z2_T_From_M = Time_Counter_Minus(Z2_T_From_H, Z2_T_From_M, 6, 7)

        # Print to display new time
        display.fill_rectangle(133, 79, 10, 32, 0xdedb)
        Font1.text(str(Z2_T_From_H)+":"+str(Z2_T_From_M), 80, 134, 1, 1)

    # + Time To
    if Button==9:
        Z2_T_To_H = int(DB_SET[str(8)].decode('utf-8'))
        Z2_T_To_M = int(DB_SET[str(9)].decode('utf-8'))
        Z2_T_To_H, Z2_T_To_M = Time_Counter_Plus(Z2_T_To_H, Z2_T_To_M, 8, 9)
        
        # Print to display new time
        display.fill_rectangle(103, 79, 10, 32, 0xdedb)
        Font1.text(str(Z2_T_To_H)+":"+str(Z2_T_To_M), 80, 104, 1, 1)

    # - Time To
    if Button==10:
        Z2_T_To_H = int(DB_SET[str(8)].decode('utf-8'))
        Z2_T_To_M = int(DB_SET[str(9)].decode('utf-8'))
        Z2_T_To_H, Z2_T_To_M = Time_Counter_Minus(Z2_T_To_H, Z2_T_To_M, 8, 9)
        
        # Print to display new time
        display.fill_rectangle(103, 79, 10, 32, 0xdedb)
        Font1.text(str(Z2_T_To_H)+":"+str(Z2_T_To_M), 80, 104, 1, 1)

    # Counter [counts]
    if Button==11:
        Z2_Counter = int(DB_SET[str(10)].decode('utf-8'))
        Z2_Counter = Counter_Plus(Z2_Counter, 10)

        # Print to display new time
        display.fill_rectangle(133, 219, 10, 20, 0xdedb)
        Font1.text(str(Z2_Counter), 220, 134, 1, 1)

    # Process time [minutes]
    if Button==12:
        Z2_Process = int(DB_SET[str(11)].decode('utf-8'))
        Z2_Process = Process_Plus(Z2_Process, 11)

        # Print to display new time
        display.fill_rectangle(103, 219, 10, 15, 0xdedb)
        Font1.text(str(Z2_Process), 220, 104, 1, 1)

    #--------------Evening--------------#
    # + Time From
    if Button==13:
        Z3_T_From_H = int(DB_SET[str(12)].decode('utf-8'))
        Z3_T_From_M = int(DB_SET[str(13)].decode('utf-8'))
        Z3_T_From_H, Z3_T_From_M = Time_Counter_Plus(Z3_T_From_H, Z3_T_From_M, 12, 13)
        
        # Print to display new time
        display.fill_rectangle(57, 79, 10, 32, 0xdedb)
        Font1.text(str(Z3_T_From_H)+":"+str(Z3_T_From_M), 80, 58, 1, 1)

    # - Time From
    if Button==14:
        Z3_T_From_H = int(DB_SET[str(12)].decode('utf-8'))
        Z3_T_From_M = int(DB_SET[str(13)].decode('utf-8'))
        Z3_T_From_H, Z3_T_From_M = Time_Counter_Minus(Z3_T_From_H, Z3_T_From_M, 12, 13)
        
        # Print to display new time
        display.fill_rectangle(57, 79, 10, 32, 0xdedb)
        Font1.text(str(Z3_T_From_H)+":"+str(Z3_T_From_M), 80, 58, 1, 1)

    # + Time To
    if Button==15:
        Z3_T_To_H = int(DB_SET[str(14)].decode('utf-8'))
        Z3_T_To_M = int(DB_SET[str(15)].decode('utf-8'))
        Z3_T_To_H, Z3_T_To_M = Time_Counter_Plus(Z3_T_To_H, Z3_T_To_M, 14, 15)
        
        # Print to display new time
        display.fill_rectangle(27, 79, 10, 32, 0xdedb)
        Font1.text(str(Z3_T_To_H)+":"+str(Z3_T_To_M), 80, 28, 1, 1)

    # - Time To
    if Button==16:
        Z3_T_To_H = int(DB_SET[str(14)].decode('utf-8'))
        Z3_T_To_M = int(DB_SET[str(15)].decode('utf-8'))
        Z3_T_To_H, Z3_T_To_M = Time_Counter_Minus(Z3_T_To_H, Z3_T_To_M, 14, 15)
        
        # Print to display new time
        display.fill_rectangle(27, 79, 10, 32, 0xdedb)
        Font1.text(str(Z3_T_To_H)+":"+str(Z3_T_To_M), 80, 28, 1, 1)

    # Counter [Counts]
    if Button==17:
        Z3_Counter = int(DB_SET[str(16)].decode('utf-8'))
        Z3_Counter = Counter_Plus(Z3_Counter, 16)

        # Print to display new time
        display.fill_rectangle(57, 219, 10, 20, 0xdedb)
        Font1.text(str(Z3_Counter), 220, 58, 1, 1)

    # Process time [minutes]
    if Button==18:
        Z3_Process = int(DB_SET[str(17)].decode('utf-8'))
        Z3_Process = Process_Plus(Z3_Process, 17)

        # Print to display new time
        display.fill_rectangle(27, 219, 10, 15, 0xdedb)
        Font1.text(str(Z3_Process), 220, 28, 1, 1)

    Font1.deinit()