any_number = int(input())
boundary_number = 100
if any_number < boundary_number:
    print("Your number is less than boundary number")
elif boundary_number < any_number < boundary_number * 3:
    print("Your number is greater than boundary number")
elif any_number > boundary_number * 3:
    print("Your number is greater than boundary number more than 3 times")
else:
    print()
