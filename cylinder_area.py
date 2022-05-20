#!/usr/bin/env python3
# Created by: Ferdous Sediqi
# Created on: May 14, 2022
# This program asks the user for the radius and
# height of the Cylinder. then, calculates and displays
# surface area of the Cylinder using a a different function
# called cylinder_area.

import math


# Declare cylinder_area with 2 prameters
def cylinder_area(radius, height):
    # calculate the surface area of cylinder
    area_fourmula1 = 2 * math.pi * radius * height
    area_fourmula2 = 2 * math.pi * radius * radius
    total_area = area_fourmula1 + area_fourmula2
    return total_area


def main():
    while True:
        # line space
        print("")
        # greet user
        print("Welcome!! in this program we ask user for height and radius")
        print("of the Cylinder and display the surface area of the Cylinder.")
        print("")
        # ask user input height and radius 
        input_height_string = input("Enter the height is (cm) ")
        input_radius_string = input("Enter the radius (cm) ")
        try:
            # convert it to float
            input_radius_float = float(input_radius_string)
            input_height_float = float(input_height_string)

            # check if user input is 0 or less
            if (input_height_float <= 0 or input_radius_float <= 0):
                print("Invalid input. Inputs cannot be 0 or less.")
            else:
                # call the cylinder_area function
                calling_function = cylinder_area(input_radius_float, input_height_float)
                print("The total surface area of the Cylinder is {:.2f}"
          .format(calling_function), "cm²")

        # display invalid input for input with no number
        except Exception:
            print("Invalid input. Input was not a number.")

        # ask user if they would like to restart the program
        play_again = input("Restart the program?(y/n or any key to End) ")
        if play_again == "y":
            continue
        else:
            break
    print("")
    print("Thank you for playing.")
    print("Have a good day.")


if __name__ == "__main__":
    main()
