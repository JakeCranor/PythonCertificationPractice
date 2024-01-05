# # Assignment Name: Constructing a Triangle Pattern with Python
# # Assignment Description:
# # The purpose of this assignment is to provide a practical exposure to Python loops and string manipulation.
# # Task:
# # Create a Python script that takes an integer input `n` and then prints a right-angled triangle of `$` symbols of height `n`.
# # Requirements:
#
# # 1. Your program should accept an integer input from the user.
# #
# # 2. If the input is not an integer or if it is less than 1, your program should display a message asking for a valid integer input greater than 0.
# #
# # 3. Your program should use loops to generate the triangle pattern.
# #
# # 4. Create a function `create_triangle(n)` to generate the triangle pattern.
# def triangle_area(integer):
#     integer = int(integer)
#     for i in range(integer + 1):
#         string = ''
#         while(i > 0):
#             string += '$'
#             i -= 1
#         print(string)
#
# integer = input("Insert Integer here: ")
# integer = integer.strip()
# while not integer.isdigit() or int(integer) < 1:
#     print("Enter valid integer greater than one")
#     integer = input("Insert Integer here: ")
# triangle_area(integer)









