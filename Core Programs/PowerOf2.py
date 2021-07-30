"""
*Author : Prathamesh Tibile
*Date   : 27-07-21
*Time   : 1-30 PM
*Title  : takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N.x
"""
def power_2(n):
    if n > 30:
        print("since 2^31 overflows an int, So enter correct number which is less than 31")
        return
    i = 1
    while i <= n:
        print(f"2^{i} result is: {2 ** i}")
        i += 1

power_2(int(input("Enter number: ")))