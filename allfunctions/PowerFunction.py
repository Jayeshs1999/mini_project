def for_Power():
    print("\nSelect your measurment -")
    print("1.Watt(W)\n2.Kilowatt(kW)")
    choice2 = int(input("Enter your choice :"))
    if (choice2 == 1 or choice2 == 2 or choice2 == 3 or choice2 == 4 or choice2 == 4):
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Power()
    print("\nIn Which -")
    print("1.Watt(W)\n2.Kilowatt(kW)")
    choice3 = int(input("Enter your choice :"))
    if (choice3 == 1 or choice3 == 2 or choice3 == 3 or choice3==4 or choice3==4):
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Power()
    if (choice2 == 1) and (choice3 == 2):
        watt = float(input("\nEnter the Power in Watt(W) :"))
        k_watt = watt / 1000
        print(f"Power in Kilowatt(kW) is :  {k_watt} kW")
    elif (choice2 == 2) and (choice3 == 1):
        k_watt = float(input("\nEnter the Power in Kilowatt(kW) :"))
        watt = k_watt * 1000
        print(f"Power in Watt(W) is :  {watt} W")
    elif (choice2 == 1) and (choice3 == 1):
        watt = float(input("\nEnter the Power in Watt(W) :"))
        print(f"Power in Watt(W) is :  {watt} W")
    elif (choice2 == 2) and (choice3 == 2):
        k_watt = float(input("\nEnter the Power in Kilowatt(kW) :"))
        print(f"Power in Kilowatt(kW) is :  {k_watt} kW")