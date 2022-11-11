# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# LINK: https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
# StackOverflow-Help: https://stackoverflow.com/questions/64478125/how-do-i-change-a-variable-in-each-iteration-in-a-list-comprehension



'''My solution'''
'''!!!!! My solution should be best !!!!!'''
'''Reason: Becasue there is no best solution like mine'''

def unique_in_order(iterable):
    k = None
    return [k :=l  for l in iterable if l != k]

# unique_in_order('AAAABBBCCDAABBB')