def for_Area():
    print("\nSelect your measurment -")
    print("1.Hectare(ha)\n2.Square meter(m**2)")
    choice2 = int(input("Enter your choice :"))
    if choice2 == 1 or choice2 == 2 or choice2 == 3 or choice2 == 4 or choice2 == 4:
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Area()
    print("\nIn Which -")
    print("1.Hectare(ha)\n2.Square meter(m**2)")
    choice3 = int(input("Enter your choice :"))
    if choice3 == 1 or choice3 == 2 or choice3 == 3 or choice3 == 4 or choice3 == 4:
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Area()

    if (choice2 == 1) and (choice3 == 2):
        ha = float(input("\nEnter the Area in Hectare(ha) :"))
        sm_2 = ha * 10000
        print(f"Area in Square meter(m**2) :  {sm_2} m^2")
    elif (choice2 == 2) and (choice3 == 1):
        sm_2 = float(input("\nEnter Area in Square meter(m**2) :"))
        ha = sm_2 / 10000
        print(f"Area in Hectare(ha) :  {ha} ha")
    elif (choice2 == 1) and (choice3 == 1):
        ha = float(input("\nEnter Area in Hectare(ha) :"))
        print(f"Area in Hectare(ha) is :  {ha} ha")
    elif (choice2 == 2) and (choice3 == 2):
        sm_2 = float(input("\nEnter Area in Square meter(m**2) :"))
        print(f"Area in Square meter(m**2) is :  {sm_2} m^2", sm_2)

#------------------------------------------------------------------------------------


