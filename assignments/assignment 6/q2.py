input_string=input("enter string: ")
check_palindrome=input_string.replace(" ", "")
reversed_string=check_palindrome[len(check_palindrome)::-1]
if reversed_string==check_palindrome:
    print("ya")
else:
    print("no")    