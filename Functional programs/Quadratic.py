"""
* AUTHOR : Prathamesh Tibile
* Date   : 29-07-21
* Time   : 2.00 PM
* Title  :Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)
"""
from math import sqrt
class QuadraticEquation:
    def __init__(self,coeficient_of_a,coeficient_of_b,coeficient_of_c):

        self.coeficient_of_a=coeficient_of_a
        self.coeficient_of_b=coeficient_of_b
        self.coeficient_of_c=coeficient_of_c

    def calculateQuadraticEquation(self):
        """
         calculate delta and root x1 and x2
        """
        delta=((self.coeficient_of_b*self.coeficient_of_b)-(4*self.coeficient_of_a*self.coeficient_of_c))
        root_value_of_x1 = (-(self.coeficient_of_b) + sqrt(abs(delta))) / (2 * self.coeficient_of_a)
        root_value_of_x2 = (- (self.coeficient_of_b) - sqrt(abs(delta))) / (2 * self.coeficient_of_a)
        return root_value_of_x1,root_value_of_x2
while True:
    try:
        coeficient_of_a = int(input("Enter the coeficient of A value : "))
        if coeficient_of_a<0:
            print("Please Enter Positive Digit")
            continue
        coeficient_of_b = int(input("Enter the coeficient of B value : "))
        if coeficient_of_b<0:
            print("Please Enter Positive Digit")
            continue
        coeficient_of_c = int(input("Enter the coeficient of C value : "))
        if coeficient_of_c<0:
            print("Please Enter Positive Digit")
            continue
        '''
            take input from user and call the methods using object 
        '''
        quadratic_equation_obj = QuadraticEquation(coeficient_of_a,coeficient_of_b,coeficient_of_c)
        result=quadratic_equation_obj.calculateQuadraticEquation()
        print("Root value are :",result)

    except ValueError:
        print("Please Enter Digit Value")
        continue

    except:
        print("Exception Occurred")
        break