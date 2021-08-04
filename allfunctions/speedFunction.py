def for_Speed():
    print("\nSelect your measurment -")
    print("1.kilometer/hour(km/h)\n2.Meter/second(m/s)")
    choice2 = int(input("Enter your choice :"))
    if (choice2 == 1 or choice2 == 2 or choice2 == 3 or choice2 == 4 or choice2 == 4):
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Speed()
    print("\nIn Which -")
    print("1.kilometer/hour(km/h)\n2.Meter/second(m/s)")
    choice3 = int(input("Enter your choice :"))
    if (choice3 == 1 or choice3 == 2 or choice3 == 3 or choice3==4 or choice3==4):
        pass
    else:
        print("\t\t\tInvalid choice ! ,Try Again ")
        return for_Speed()
    if (choice2 == 1) and (choice3 == 2):
        km_h = float(input("\nEnter the Speed in kilometer/hour(km/h) :"))
        m_s = km_h * (5 / 18)
        print(f"Speed in Meter/second(m/s) is :  {m_s} m/s")
    elif (choice2 == 2) and (choice3 == 1):
        m_s = float(input("\nEnter the speed in Meter/second(m/s) :"))
        km_h = m_s * (18 / 5)
        print(f"Speed in kilometer/hour(km/h) is :  {km_h} km/h")
    elif (choice2 == 1) and (choice3 == 1):
        km_h = float(input("\nEnter the Speed in kilometer/hour(km/h) :"))
        print(f"Speed in kilometer/hour(km/h) is :  {km_h} km/h")
    elif (choice2 == 2) and (choice3 == 2):
        m_s = float(input("\nEnter the speed in Meter/second(m/s) :"))
        print(f"Speed in Meter/second(m/s) is :  {m_s} m/s")