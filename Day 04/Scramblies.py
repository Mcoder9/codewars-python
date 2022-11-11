# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

'''My Solution One not Efficient'''

def scramble(str1,str2):
    check = [str2.count(l) <= str1.count(l)  for l in str2]
    return False not in check
    
scramble('katas','steak')


'''My Second Solution not Efficient'''

def scramble(str1,str2):
    str1 = list(str1)
    check = [l == str1.pop(str1.index(l)) if l in str1 else False for l in str2]
    return False not in check
scramble('katas','steak')


'''My Third Solution not Efficient'''

def scramble(str1,str2):
    str1 = list(str1)
    return False not in [str1.remove(l) if l in str1 else False for l in str2]

scramble('cedewaraaossoqqyt','codewars')
