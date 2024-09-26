def temp_conversion():

    temp = float(input("Enter a temperature. "))
    conversion = (input("Select a conversion type.  f to c or c to f only: ")).strip()

    if conversion == "c to f":
        conversion_temp = (temp * 9/5) + 32
        print(f"{temp}celcius is equal to {conversion_temp}fahrenheit")

    elif conversion == "f to c":
        conversion_temp = (temp - 32) * 5/9
        print(f"{temp} fahrenheit is equal to {conversion_temp} celcius")

    else:
        print("Invalid input please try again")

temp_conversion()