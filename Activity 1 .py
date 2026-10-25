print("============================================================")
print("              Welcome To The Ride Builder!                        ")
print("============================================================")
print()

print("Step 1: Pick Your Vehicle")
print(" 1: Bike")
print(" 2: Car")
print()

choice =int(input("Enter 1 Or 2 :"))
print()

if choice == 1:
    print("Step 2:Pick Your Bike Type")
    print("1 - Scooty")
    print("2- Mountain Bike")
    print()

    bike_type=int(input("Enter 1 or 2 :"))
    if bike_type == 1:
        print("You Picked   :Scooty")
        print("Top Speed    :80kmph")
        print("Best For     :City Roads")
    else:
        print("You Picked:    Mountain Bike")
        print("Top Speed:     40kmph")
        print("Best for       Off-Road       ")

elif choice==2:
    print("Step 2:Pick Your Car Type")
    print("1 -Sedan")
    print("2-SUV")
    print()
    
    car_type=int(input("Enter 1 or 2:"))
    print()

    if car_type ==1:
       print("You Picked : Sedan")
       print("Seats: 5 passengers")
       print("Best For: Family Trip")
       
    else:
        print("You Picked: SUV")
        print("Seats:7 seats ")
        print("Best for: Off Road Adventure")
else:
    print("That Was Not A Valid Choice ")
    print("Please Enter 1 for Bike Or 2 For Car")

print()
print("==========================================")
print("Your Custom Ride Is Ready!")
print("Enjoy The Journey")
print("==========================================")
