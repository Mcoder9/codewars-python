# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


# Note: For 4 or more names, the number in "and 2 others" simply increases.

# Codewars Function

# def likes(names):
#     #your_code_is_here
#     pass


names = ["Alex", "Jacob", "Mark", "Max"]

def likes(names):

    action = 'likes' if len(names)<=1 else 'like'
    if len(names) == 0: display = f"no one {action} this"
    elif len(names) == 3: display = f"{names[0]}, {' and '.join(names[1:])} {action} this"
    elif 0<len(names)<3 : display = f"{' and '.join(names)} {action} this"
    else: display = f'{names[0]}, {names[1]} and {len(names[2:])} others {action} this'

    return display