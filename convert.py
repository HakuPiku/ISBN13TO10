def ISBN13TO10(a) : 
     #Strip the dashes
    a = a.replace("-", "")
    #If ISBN13 field already has the ISBN10 then return it
    if len(a) < 13 :
        return a
    else:
        a = a[3:12]
        b = list(a)
        sum = 0
        #Do the math (first digit * 10 , second digit * 9 ... last digit * 2)
        for x in range(0, 9):
            b[x] = (10-x)* int(b[x])
            #Take the sum of the new values
            sum +=int(b[x])
        #The last digit in the ISBN10 will be 11 minus 11 mod the sum.
        lastDig = 11 - (sum % 11)
        #If the last digit is 10 then concatenate the roman symbol for 10 - X 
        if lastDig == 10 :
            a = a + 'X'
        #If the last digit is 11 then take concatenate 0
        elif lastDig == 11:
            lastDig = 0
            a = a + str(lastDig)
        #Otherwise concatenate the last digit itself.
        else : 
            a = a + str(lastDig)
        return a
