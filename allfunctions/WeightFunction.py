def for_Weight():
    print("\nSelect your measurment -")
    print("1.Kilogram(kg)\n2.Gram(g)")
    choice2 = int(input("Enter your choice :"))
    if choice2 == 1 or choice2 == 2 or choice2 == 3 or choice2 == 4 or choice2 == 4:
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Weight()
    print("\nIn Which -")
    print("1.Kilogram(kg)\n2.Gram(g)")
    choice3 = int(input("Enter your choice :"))
    if choice3 == 1 or choice3 == 2 or choice3 == 3 or choice3==4 or choice3==4:
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Weight()
    if (choice2 == 1) and (choice3 == 2):
        kg = float(input("\nEnter the Weight in Kilogram :"))
        g = kg * 1000
        print(f"Weight in Gram(g) is :  {g} g")
    elif (choice2 == 2) and (choice3 == 1):
        g = float(input("\nEnter the Weight in Gram(g) :"))
        kg = g / 1000
        print(f"Weight in Kilogram(kg) is :  {kg} kg")
    elif (choice2 == 1) and (choice3 == 1):
        kg = float(input("\nEnter the Weight in Kilogram :"))
        print(f"lenght in Kilogram(kg) is : {kg} kg")
    elif (choice2 == 2) and (choice3 == 2):
        g = float(input("\nEnter the Weight in Gram(g) :"))
        print(f"Weight in Gram(g) is :  {g} g")
