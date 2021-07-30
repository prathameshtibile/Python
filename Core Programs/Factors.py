"""
*Author : Prathamesh Tibile
*Date   : 28-07-21
*Time   : 10-30 AM
*Title  :Print the prime factors of number N.
"""
Number = int(input("Enter an integer:"))
print(" Prime Factors are: ")

i = 2;
while(Number != 1):
    rem = Number % i
    if (rem ) == 0:
        Number = Number/i;
        print(i)
    else:
        i = i+1;




