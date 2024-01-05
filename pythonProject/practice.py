# """
#
# Create a method called twelver that accepts 2 integer arguments: a and b.
# The method should return True if one of the arguments is 12
# or if the sum of both arguments equals 12.
#
# twelver(3, 12) → True
# twelver(4, 9) → False
# twelver(9, 3) → True
#
# """
#
# def twelver(a, b):
#     if a == 12 or b == 12:
#         return True
#     elif a + b == 12:
#         return True
#     else:
#         return False
# print(twelver(3, 12))
# print(twelver(4, 9))
# print(twelver(9, 3))
#
# """
# Create a method called pay_extra that accepts 2 parameters:
#  working, and hour. This method will be used to decide whether
#  an employee will receive extra pay or not. If an employee is working
#  during the hrs of 8pm until 8am in the morning, that means they
#  should be paid extra. In that situation the method should return true,
#  otherwise it should return false.
#
#  NOTE: the hour parameter should be from 0-23.
#         So 8AM is hour 8, and 8PM is hour 20.
#
# Example:
#     pay_extra(True, 11) -> false
#     pay_extra(False, 5) -> false
#     pay_extra(True, 6)  -> true
# """
#
# def pay_extra(working, hour):
#     if (working == True and (hour > 20 or hour < 8)):
#         return True
#     else:
#         return False
# print(pay_extra(True, 11))
# print(pay_extra(False, 5))
# print(pay_extra(True, 6))

# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""
#
# # Your Code Below:
# def sequence(list_a):
#     if len(list_a) < 3:
#         return False
#     else:
#         for items in range(1, len(list_a) - 1):
#             if list_a[items] == 2 and list_a[items + 1] == 3 and list_a[items - 1] == 1:
#                 return True
#         return False
# print(sequence([1, 1]))
# print(sequence([1, 2, 3]))
# print(sequence([1, 1, 2, 3, 1]))
# print(sequence([1, 1, 2, 4, 1]))
# print(sequence([1, 1, 2, 1, 2, 3]))
# Assignment 4
# """
# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
# grow_string('Code') → 'CCoCodCode'
# grow_string('abc') → 'aababc'
# grow_string('ab') → 'aab'
#
# """
# # Your Code Below:
# def grow_string(word):
#     word_return = ''
#     x = 1
#     for items in word:
#         word_return += word[0:x]
#         x += 1
#     return word_return
# print(grow_string('Code'))
# print(grow_string(''))
# print(grow_string('a'))
# print(grow_string('ab'))
# print(grow_string('abc'))

# Assignment 5
#
# """
# Define a method that accepts a list as an argument
# and returns True if one of the first_folder 4 elements
# in the list is a 6. The list length may be less than 4.
#
#
# first3([1, 2, 6, 3, 4]) → True
# first3([1, 2, 3, 4, 6]) → False
# first3([1, 2, 3, 4, 5]) → False
#
# """
#
# # Your Code Below:
# def first3(list_a):
#     if len(list_a) < 4:
#         for i in range(len(list_a)):
#             if list_a[i] == 6:
#                 return True
#     else:
#         for i in range(4):
#             if list_a[i] == 6:
#                 return True
#     return False
#
#
# print(first3([1,2,6,3,0,0])) # true
# print(first3([1,2,3,3,0,6])) # false
# print(first3([6])) # true
# print(first3([])) # false

# # Assignment 6
#
# """
# Create a function called last2 that accepts a string argument.
# The function should return the count of the number of times that the last
# 2 characters appear in the rest of the string. You should not count
# the last 2 characters as an occurrence. The last 2 characters is just the
# sequence your function should look for in the remaining string.
#
# So "hixxxhi" yields 1 (we won't count the end substring).
#
#
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2
#
# """
#
# # Your Code Below:
# def last2(word):
#     if len(word) < 4:
#         return 0
#     look = word[-2:]
#     counter = 0
#     for i in range(len(word)-3):
#         if word[i:i+2] == look:
#             counter += 1
#     return counter
#
# def hislast2(str):
#     # Screen out too-short string case.
#     if len(str) < 2:
#         return 0
#
#     # last 2 chars, can be written as str[-2:]
#     last2 = str[len(str) - 2:]
#     count = 0
#
#     # Check each substring length 2 starting at i
#     for i in range(len(str) - 2):
#         sub = str[i:i + 2]
#         if sub == last2:
#             count = count + 1
#
#     return count
# print(last2('iiii'))
# print(hislast2('iiii'))
# print(last2('hixxhi')) #→ 1
# print(last2('xaxxaxaxx')) #→ 1
# print(last2('axxxxaaxx')) #→ 3

# # Assignment 7
# """
# Given 2 strings, a and b, return the number of the positions where
# they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
# yields 3, since the "xx", "aa", and "az" substrings appear in the same
# place in both strings.
#
# EXAMPLE:
#     string_match('xxcaazz', 'xxbaaz') → 3
#     string_match('abc', 'abc') → 2
#     string_match('abc', 'axc') → 0
#
# """
#
# #Your Code Below:
# def string_match(a, b):
#     x = 0
#     counter = 0
#     if len(a) < len(b):
#         x = len(a)
#     else:
#         x = len(b)
#     for i in range(x - 1):
#         if a[i : i+2] == b[i : i+2]:
#             counter += 1
#     return counter
# print(string_match('xxcaazz', 'xxbaaz'))
# print(string_match('abc', 'abc'))
# print(string_match('', ''))
# print(string_match('abc', 'axc'))
#
#
#
# # Assignment 8
#
# """
#
# Return the sum of the numbers in the list, except ignore sections of
# numbers starting with a 7 and extending to the next 8
# (every 7 will be followed by at least one 8).
# Return 0 for no numbers.
#
# EXAMPLE:
# sum78([1, 2, 2]) → 5
# sum78([1, 2, 2, 7, 99, 99, 8]) → 5
# sum78([1, 1, 7, 8, 2]) → 4
#
# """
#
# #Your Code Below:
# def sum78(nums):
#     sum_result = 0
#     isSeven = False
#     for num in nums:
#         if num == 8:
#             isSeven = False
#             continue
#         elif num == 7:
#             isSeven = True
#             continue
#         elif isSeven:
#             continue
#         else:
#             sum_result += num
#     return sum_result
#
# print(sum78([1, 2, 2, 7, 99, 99, 8]))
# print(sum78([1, 1, 7, 8, 2]))
# print(sum78([1, 2, 2]))

# # Assignment 9
#
# """
# We have 2 variables. fr and d. fr is a list of strings and d is a dictionary with email
# addresses as keys and numbers as values (numbers in string format).
# Write code to replace the email address in each of the strings in the fr list with
# the associated value of that email looked up from the dictionary d.
# If the dictionary does not contain the email found in the list, add a new entry
# in the dictionary for the email found in the fr list. The value for this new email key
# will be the next highest value number in the dictionary in string format.
#
# Once the dictionary is populated with this new email key and a new number value,
# replace that email's occurrence in the fr list with the number value.
#
# The output of running your completed code should be the following:
#
# Value of fr:
# ['199|4|11|GDSPV', '199|16|82|GDSPV', '205|12|82|GDSPV', '206|19|82|GDSPV']
# Value of d:
# {'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205', '26@comp1.COM': '206'}
#
# """
#
# # Don't manually change fr and d.
# fr = [
# '7@comp1.COM|4|11|GDSPV',
# '7@comp1.COM|16|82|GDSPV',
# '13@comp1.COM|12|82|GDSPV',
# '26@comp1.COM|19|82|GDSPV'
# ]
#
# d= {
# '7@comp1.COM': '199',
# '8@comp4.COM': '200',
# '13@comp1.COM': '205'
# }
#
#
# # Your Code Below:
# # --------------------------------------
# for i in range(len(fr)):
#     string = ''
#     for letter in fr[i]:
#         if letter == "|":
#             break
#         string += letter
#     if d.get(string) is not None:
#         stringReplacement = d.get(string)
#         fr[i] = str(stringReplacement) + str(fr[i][len(string):])
#     else:
#         next_num = int(max(d.values())) + 1
#         d.update({string: next_num})
#         stringReplacement = d.get(string)
#         fr[i] = str(stringReplacement) + str(fr[i][len(string):])
#
# # don't change the lines below:
# # --------------------------------------
# print("Value of fr: ")
# print(fr)
# print("Value of d:")
# print(d)







