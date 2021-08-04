def for_Volume():
    print("\nSelect your measurment -")
    print("1.Liter(l)\n2.Milliliter(ml)")
    choice2 = int(input("Enter your choice :"))
    if choice2 == 1 or choice2 == 2 or choice2 == 3 or choice2 == 4 or choice2 == 4:
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Volume()
    print("\nIn Which -")
    print("1.Liter(l)\n2.Milliliter(ml)")
    choice3 = int(input("Enter your choice :"))
    if choice3 == 1 or choice3 == 2 or choice3 == 3 or choice3 == 4 or choice3 == 4:
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Volume()
    if (choice2 == 1) and (choice3 == 2):
        liter = float(input("\nEnter the Volume in liter(ml) :"))
        ml = liter * 1000
        print(f"Volume in milliliter(ml) is :  {ml} ml")
    elif (choice2 == 2) and (choice3 == 1):
        ml = float(input("\nEnter Volume in milliliter(ml) is :"))
        liter = ml / 1000
        print(f"Volume in liter(ml) :  {liter} ml")
    elif (choice2 == 1) and (choice3 == 1):
        liter = float(input("\nEnter Volume in liter(ml) :"))
        print(f"Volume in liter(ml) is :  {liter} ml")
    elif (choice2 == 2) and (choice3 == 2):
        ml = float(input("\nEnter Volume in milliliter(ml) :"))
        print(f"Volume in milliliter(ml) is :  {ml} ml")
