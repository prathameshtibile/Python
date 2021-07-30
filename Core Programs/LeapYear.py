"""
*Author : Prathamesh Tibile
*Date   : 27-07-21
*Time   : 11-00 AM
*Title  : To check wheather the year is leap or not.
"""

Year = int(input("Enter a year :"))
if (Year % 400) ==0 or (Year % 4) == 0 or (Year % 100) == 0:
    print("{0} is a leap year".format(Year))
else:
     print("{0} is not a leap year".format(Year))


