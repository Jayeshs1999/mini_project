from allfunctions.AreaFunction import for_Area
from allfunctions.PowerFunction import for_Power
from allfunctions.VolumeFunction import for_Volume
from allfunctions.WeightFunction import for_Weight
from allfunctions.lenghtFunction import for_Lenght
from allfunctions.speedFunction import for_Speed

print("\n")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t* UNIT CONVERTER PROJECT *")

def Greeting_message():
    print("\n\nThank You ,Best of luck !!")
    print("Continue again......")

while True:
    print("\nUnit Conversion -")
    print("------------------------------------------------------------------------------------------------------")
    print("1.Length\n2.Area\n3.Volume\n4.Speed\n5.Weight\n6.Temperature\n7.Power\n8.Pressure\n9.Exit")
    print("------------------------------------------------------------------------------------------------------")
    choice = int(input("Enter your choice :"))
    print("------------------------------------------------------------------------------------------------------")

    if choice == 1:
        for_Lenght()
        Greeting_message()

    elif choice == 2:
        for_Area()
        Greeting_message()

    elif choice == 3:
        for_Volume()
        Greeting_message()

    elif choice == 4:
        for_Speed()
        Greeting_message()

    elif choice == 5:
        for_Weight()
        Greeting_message()

    elif choice == 7:
        for_Power()
        Greeting_message()

    elif choice == 9:
        quit()

    else:
        print("Sorry, please Enter valid Choice !!")
