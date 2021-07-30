"""
* AUTHOR : Prathamesh Tibile
* Date   : 29-07-21
* Time   : 11.00 PM
* Title  : A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
"""
def triplet(array, array_len, sum):
    for i in range(0, array_len - 2):
        for j in range(i + 1, array_len - 1):
            for k in range(j + 1, array_len):
                if array[i] + array[j] + array[k] == sum:
                    print(array[i], array[j], array[k])


array = list(map(int, input('Enter te value :').split()))
array_len = len(array)
sum = 0
triplet(array, array_len, sum)