"""
* AUTHOR : Prathamesh Tibile
* Date   : 29-07-21
* Time   : 11.00 PM
* Title  :Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:

Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).
"""

try:
    while True:
        temperature = int(input("Enter the Temperature from '0' to '50':"))
        if (temperature >= 0) and (temperature <= 50):
            print()
            windSpeed = int(input("Enter the Wind Speed between '3' to '120' : "))
            if (windSpeed >= 3) and (windSpeed <= 120):
                windChill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * pow(windSpeed, 0.16)
                #  formula to calculate Wind Chill Using Parameter temperature and Wind speed
                print()
                print("Temperature = ", temperature)
                print("Wind speed  = ", windSpeed)
                print("Wind chill  = ", windChill)
                print()
            else:
                print("Enter the Valid Wind Speed")
        else:
            print("Enter the Valid Temperature")
            print()
except ValueError:
    print("Please give the Valid input as Shown in the Statement above!!")
    print()
except KeyboardInterrupt:
    print()
    print("Force Quit!!!!")