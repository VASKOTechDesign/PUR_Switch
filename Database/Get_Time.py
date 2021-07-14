def Get_Time():
    import machine

    #Read Time and RPM
    rtc = machine.RTC()
    _Current_Time = rtc.datetime()

    #Year
    Year = str(_Current_Time[0])

    #Month
    Month = _Current_Time[1]
    if Month<10:
        Month = "0"+str(_Current_Time[1])
    else:
        Month = str(_Current_Time[1])

    #Day
    Day = _Current_Time[2]
    if Day<10:
        Day = "0"+str(_Current_Time[2])
    else:
        Day = str(_Current_Time[2])

    #Week day

    #Hour
    Hour = _Current_Time[4]
    if Hour<10:
        Hour = "0"+str(_Current_Time[4])
    else:
        Hour = str(_Current_Time[4])

    #Minutes
    Minutes = _Current_Time[5]
    if Minutes<10:
        Minutes = "0"+str(_Current_Time[5])
    else:
        Minutes = str(_Current_Time[5])

    Date_Time = [str(Year), str(Month), str(Day), str(Hour), str(Minutes)]

    return Date_Time
