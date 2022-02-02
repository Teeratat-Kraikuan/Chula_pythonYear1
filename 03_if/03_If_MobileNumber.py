nbr = input()

if nbr[0:2] in ["06", "08", "09"] and len(nbr) == 10:
    print("Mobile number")
else:
    print("Not a mobile number")