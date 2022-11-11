# URL : https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/python
# DESCRIPTION:
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))


'''My solution'''

def plus(inputNum): return str(inputNum)+'+'
def minus(inputNum): return str(inputNum)+'-'
def times(inputNum): return str(inputNum)+'*'
def divided_by(inputNum): return str(inputNum)+'/'

def zero(params=None): return int(eval(f'{params}0')) if params else 0
def one(params=None): return int(eval(f'{params}1')) if params else 1
def two(params=None): return int(eval(f'{params}2')) if params else 2
def three(params=None): return int(eval(f'{params}3')) if params else 3
def four(params=None): return int(eval(f'{params}4')) if params else 4
def five(params=None): return int(eval(f'{params}5')) if params else 5
def six(params=None): return int(eval(f'{params}6')) if params else 6
def seven(params=None): return int(eval(f'{params}7')) if params else 7
def eight(params=None): return int(eval(f'{params}8')) if params else 8
def nine(params=None): return int(eval(f'{params}9')) if params else 9

print(eight(minus(three())))



