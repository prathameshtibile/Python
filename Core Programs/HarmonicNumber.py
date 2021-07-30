"""
*Author : Prathamesh Tibile
*Date   : 28-07-21
*Time   : 10-00 AM
*Title  : -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N.
"""

def harmonic(k):
        i = 1
        s = 0.0
        for i in range(1, k + 1):
            s = s + 1 / i;
        return s;

print(harmonic(int(input("Enter the number:"))))

