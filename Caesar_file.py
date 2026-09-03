def choice(name):
    while True:
        print(f"1.{name} Text")
        print(f"2.{name} File")
        try:
            y=int(input("Enter Your Choice:"))
        except ValueError:
            print("Please enter a number")
            continue
        if (y!=1 and y!=2):
            print("Enter Either 1 or 2")
            continue
        break
    while (True):
        print("1.Caesar")
        print("2.Vignere")
        try:
            z=int(input("Enter Your Choice:"))
        except ValueError:
            print("Please enter a number")
            continue
        if (z!=1 and z!=2):
            print("Enter Either 1 or 2")
            continue
        break
    return y,z
while True:
    print("="*300)
    print(" "*120,"CIPHER TOOL - Caesar and Vignere")
    print("1.Encrypt")
    print("2.Decrpyt")
    print("3.Exit")
    print("="*300)
    try:
        x=int(input("Enter Your Choice:"))
    except ValueError:
        print("Please enter a number")
        continue
    if x==1:
        y,z=choice("Encrypt")
        if (y == 1):
            if (z == 1):
                pass
                # call Encrypt text caesar file
            else:
                pass
                # call Encrypt file caesar file
        else:
            if (z == 1):
                pass
                # call Encrypt text vignere file
            else:
                pass
                # call Encrypt file vignere file
    elif x==2:
        y,z=choice("Decrypt")
        if (y == 1):
            if (z == 1):
                pass
                # call Decrypt text caesar file
            else:
                pass
                # call Decrypt file caesar file
        else:
            if (z == 1):
                pass
                # call Decrypt text vignere file
            else:
                pass
                # call Decrypt file vignere file
    elif x==3:
        break
    else:
        print("Enter Either 1 or 2 or 3")
        continue

