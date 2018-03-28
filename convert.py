def ISBN13TO10(a) : 
    a = a.replace("-", "")
    #If ISBN13 field already has the ISBN10 then return it
    if len(a) < 13 :
        return a
    else:
        a = a[3:12]
        b = list(a)
        sum = 0
        #Do the math
        for x in range(0, 9):
            b[x] = (10-x)* int(b[x])
            sum +=int(b[x])

        lastDig = 11 - (sum % 11)
        if lastDig == 10 :
            a = a + 'X'
        elif lastDig == 11:
            lastDig = 0
            a = a + str(lastDig)
        else : 
            a = a + str(lastDig)
        return a
