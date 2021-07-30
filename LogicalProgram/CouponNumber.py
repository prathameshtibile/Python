"""
*Author : Prathamesh Tibile
*Date   : 29-07-21
*Time   : 07-00 PM
*Title  : a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
b. I/P -> N Distinct Coupon Number
c. Logic -> repeatedly choose a random number and check whether it's a new one.
d. O/P -> total random number needed to have all distinct numbers.
e. Functions => Write Class Static Functions to generate random number and to
process distinct coupons.
"""
import random
class CouponNumber():

    def __init__(self,take_number):
        """
            constructor initialize using parameter
        """
        self.take_number=take_number

    def calculateDistinctNumber(self):

        distict_number=[]
        while len(distict_number)<self.take_number:
            rand = random.randrange(0, self.take_number)
            if  rand not in distict_number:
                distict_number.append(rand)
            else:
                pass
        return distict_number

while True:
    try:
        take_number=int(input("Enter the distinct number : "))
        if take_number<0:
            print("Please Enter Positive Digits")
            continue
            """
                taking input from user
            """
        coupon_number_object=CouponNumber(take_number)
        total_random_number=coupon_number_object.calculateDistinctNumber()
        print("Total Distinct Coupon Number : ",total_random_number)
    except ValueError:
        print("Please Enter Digit Value")
    except:
        print("Exception Occured")