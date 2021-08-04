
def for_Lenght():
    print("\nSelect your measurment -")
    print("1.Meter(m)\n2.Kilometer(km)\n3.Centimeter(cm)\n4.mile(mi)")
    choice2 = int(input("Enter your choice :"))
    if(choice2==1 or choice2==2 or choice2==3 or choice2==4 or choice2==4):
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Lenght()
        # print("Process finished with exit code 0, try again !")
        # exit()
    print("\nIn Which -")
    print("1.Meter(m)\n2.Kilometer(km)\n3.Centimeter(cm)\n4.mile(mi)")
    choice3 = int(input("Enter your choice :"))

    if (choice3 == 1 or choice3 == 2 or choice3 == 3 or choice3==4 or choice3==4):
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Lenght()

    if (choice2 == 1) and (choice3 == 2):
        meter = float(input("\nEnter the length in meter :"))
        km = meter / 1000
        print("------------------------------------------------------")
        print(f"lenght in Kilometer is :  {km} km")
        print("------------------------------------------------------")
    elif (choice2 == 2) and (choice3 == 1):
        km = float(input("\nEnter the length in kilometer :"))
        m = km * 1000
        print(f"lenght in meter is :  {m} m")
    elif (choice2 == 1) and (choice3 == 1):
        meter = float(input("\nEnter the length in meter :"))
        print(f"lenght in meter is :  {meter}")
    elif (choice2 == 2) and (choice3 == 2):
        km = float(input("\nEnter the length in kilometer :"))
        print(f"lenght in Kilometer is :  {km} km")

#-------------------Centimeter------------------------------------------
    elif (choice2 == 1) and (choice3 == 3):
        m = float(input("\nEnter the length in meter(m) :"))
        cm = m * 100
        print(f"lenght in Centimeter(cm) is :  {cm} cm")
    elif (choice2 == 3) and (choice3 == 1):
        cm = float(input("\nEnter the length in Centimeter(cm) :"))
        m = cm/100
        print(f"lenght in meter(m) is :  {m} m")
    elif (choice2 == 2) and (choice3 == 3):
        km = float(input("\nEnter the length in kilometer :"))
        cm=km*100000
        print(f"lenght in Centimenter(cm) is :  {cm} cm")

    elif (choice2 == 3) and (choice3 == 2):
        cm = float(input("\nEnter the length in Centimeter(cm) :"))
        km = cm/100000
        print(f"lenght in kilometer(km) is :  {km} km")
    elif (choice2 == 3) and (choice3 == 3):
        cm = float(input("\nEnter the length in Centimeter(cm) :"))
        print(f"lenght in Centimeter(cm) is :  {cm} cm")

#---------------------------miles---------------------------------------------------------

    elif (choice2 == 1) and (choice3 == 4):
        m = float(input("\nEnter the length in meter(m) :"))
        mi = m * 0.0006214
        print(f"lenght in Miles(mi) is :  {mi} mi", )
    elif (choice2 == 4) and (choice3 == 1):
        mi = float(input("\nEnter the length in Mile(mi) :"))
        m = mi / 0.0006214
        print(f"lenght in meter(m) is :  {m} m")
    elif (choice2 == 2) and (choice3 == 4):
        km = float(input("\nEnter the length in kilometer(km) :"))
        mi = km * 0.6214
        print(f"lenght in Mile(mi) is :  {mi} mi")

    elif (choice2 == 4) and (choice3 == 2):
        mi = float(input("\nEnter the length in Mile(mi) :"))
        km = mi * 1.609269391696169939
        print(f"lenght in kilometer(km) is :  {km} km")
    elif (choice2 == 3) and (choice3 == 4):
        cm = float(input("\nEnter the length in Centimeter(cm) :"))
        mi = cm * 0.000006214
        print(f"lenght in mile(mi) is :  {mi} mi")

    elif (choice2 == 4) and (choice3 == 3):
        mi = float(input("\nEnter the length in Mile(mi) :"))
        cm = mi / 0.000006214
        print(f"lenght in Centimeter(cm) is :  {cm} cm")
    elif (choice2 == 4) and (choice3 == 4):
        mi = float(input("\nEnter the length in Mile(mi) :"))
        print(f"lenght in Mile(mi) is :  {mi} mi")



# ------------------------------------------------------------------------------------


