"""
*Author : Prathamesh Tibile
*Date   : 27-07-21
*Time   : 11-00 AM
*Title  : Flip Coin and print percentage of Heads and Tails
"""
import random

def flipcoin(flip_time_number):
    if flip_time_number < 0:
        return "Please Enter positive number"
    head = 0
    tail = 0
    for i in range(flip_time_number):
        times = random.uniform(0, 1)
        if times <= 0.5:
            print(f"tail: {times}")
            tail += 1
        else:
            print(f"head: {times}")
            head += 1
    return f"number of head: {head}", f"number of tail: {tail}", \
           f"percentage of head vs tail is : {(abs(head - tail)) / tail*100}"

print(flipcoin(int(input("Enter the number of times to flip the coin: "))))