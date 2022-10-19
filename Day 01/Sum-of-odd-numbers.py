# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8

'''My Solution'''

def row_sum_odd_numbers(line):
    count = 0
    for x in range(1,line+1): count+=x
    return sum([2 * i - 1 for i in range(1, count+1)][-line::])

'''Best solutions'''

def row_sum_odd_numbers(n):
    #your code here
    return n ** 3

def row_sum_odd_numbers(n):
    if type(n)==int and n>0:
        return n**3
    else:
        return "Input a positive integer"