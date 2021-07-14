def Dra_Icon (A,B,C,D,E,color,display):
    Line_Index = 1
    Index_In_Line = 1
    Index = 0

    while Index<(A*B):
        if E[Index] == 49:
            Line_Index = (Index // A)
            Index_In_Line = Index - (((Index//A)*A))
            display.pixel((Line_Index+D), (Index_In_Line+C), color)   
        Index = Index + 1
