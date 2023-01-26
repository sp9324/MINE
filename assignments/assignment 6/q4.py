input_string = input("enter string: ")
new_string = input_string.replace(" ", "")

# def check_letter(ch):
#     for i in range(0, len(input_string)):
#         if input_string[i]==ch:
#             return True
#     return False


# check=True
# for ch in range(chr(97), chr(122)):
#     if check_letter(ch):
#         continue
#     else:
#         check=False
#         break

# if check:
#     print("panagram!!!")
# else:
#     print("not a panagram...")

# check_pangram=True
# check="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in range(0, len(input_string)):
#     for j in range(0, len(check)):
#         if input_string[i]!=check[j]:
#             check_letter=False
#         if input_string==check[j]:
#             check_letter=True
#             break

# if check_pangram:
#     print("pangram!!!")
# else:
#     print("not a pangram...")


# # Program to count the number of
# unique characters in a string
def cntDistinct(st):

    # Set to store unique characters
    # in the given string
    s = set([])

    # Loop to traverse the string
    for i in range(len(st)):

        # Insert current character
        # into the set
        s.add(st[i])

    # Return Answer
    return len(s)


if cntDistinct(new_string) == 26:
    print("pangram")
else:
    print("nooo")
