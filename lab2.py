################### q1 ##########################
"""
Calculate Area
Write a function that calculate the area of these shapes:
triangle    = (0.5   * base * height)
rectangle   = (width * height)
Square      = (side  * side)
Circle      = (PI    * radius ^ 2)

Input       | string    | number    | number
Triangle    | "t" - "T" | 10        | 7  
Rectangle   | "r" - "R" | 10        | 7   
Square      | "s" - "S" | 10        | -  
Circle      | "c" - "C" | 10        | -  

"""


# (*** solution ***)
import math


def calculate_area(shape, dimension1, dimension2=0):
    if shape == "t":
        area = 0.5 * dimension1 * dimension2
        text = f"Area of Triangle:-  ({area})"

    elif shape == "r":
        area = dimension1 * dimension2
        text = f"Area of Rectangle:- ({area})"

    elif shape == "s":
        area = dimension1 * dimension1
        text = f"Area of Square:-    ({area})"

    elif shape == "c":
        area = math.pi * (dimension1**2)
        text = f"Area of Circle:-    ({area})"

    else:
        return "Invalid shape"

    return text


print(calculate_area("t", 10, 7))
print(calculate_area("r", 10, 7))
print(calculate_area("s", 10))
print(calculate_area("c", 10))
print(calculate_area("x", 10))
print("#" * 50)

################### Q2 ##########################
"""
Write a function that takes a string and a character as an argument. The function should return a list of all the indices where the character appears in the string.

Input       | string                | character
            | "This is javaScript"  | "i"    

"""


# (*** solution ***)
def string(string, input):
    list = []
    for char in range(int(len(string))):
        if string[char] == input:
            list.append(char)
    return list


q2_string = "This is javaScript"
q2_input = input("Enter one letter:- ")
print(string(q2_string, q2_input))
print("#" * 50)

################### q3 ##########################
"""
Write a function that takes a number as an argument and returns a multiplication table of that number.

Input       | number
            | 3

Output      | [[1], [2, 4], [3, 6, 9]]

"""


# (*** solution ***)
def multiplication_table(nnumber):
    table = []
    for i in range(1, nnumber + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        table.append(row)
    return table


q3_input = int(input("Enter a number from 1 to 12:- "))
print(multiplication_table(q3_input))
print("#" * 50)


################### q4 ##########################
"""
Write a function that takes a list of names as an argument and returns a dictionary where the keys are the first letters of the names and the values are lists of the names that start with that letter.

Input       | list of names
            | ["ahmed", "fatma", "Ibrahim"]    

Output      | {'a': ['ahmed'], 'f': ['fatma'], 'i': ['Ibrahim']}

"""


# (*** solution ***)
def names_to_dictionary(names_list):
    sorted_dict = {}
    for name in names_list:
        first_letter = name[0].lower()
        if first_letter not in sorted_dict:
            sorted_dict[first_letter] = []
        sorted_dict[first_letter].append(name)
    return sorted_dict


q4_user_input = input('Enter a list of names (e.g., ["ahmed", "fatma", "Ibrahim"]): ')
q4_names_list = q4_user_input.strip("[]").replace('"', "").replace("'", "").split(", ")
result = names_to_dictionary(q4_names_list)
print(result)
print("#" * 50)
