def swap_first_two_characters(str1, str2):

    if len(str1) >= 2 and len(str2) >= 2:
        new_str1 = str2[:2] + str1[2:]
        new_str2 = str1[:2] + str2[2:]
        return new_str1, new_str2
    else:
        return "Strings must have at least two characters each."

str = input("Enter two strings separated by a space: ")
str1, str2 = str.split()

res1, res2 = swap_first_two_characters(str1, str2)

print("Swapped strings:")
print(res1, res2)
