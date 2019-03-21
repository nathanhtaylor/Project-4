fold = 0
fnew = 1
fplaceholder = 0
fnum = 0
farray = []

fnumraw = input("Give me a num ")

if fnumraw.isdigit():
    fnum = int(fnumraw)
    fplaceholder = fnew + fold    

    if fold < fnum:
        farray.append(fold)
    
    if fnew < fnum:
        farray.append(fnew)

    
    while fplaceholder <= fnum:
        farray.append(fplaceholder)
        fold = fnew
        fnew = fplaceholder
        fplaceholder = fnew + fold

    print (farray)

else:
    print ("You must input a positive number")