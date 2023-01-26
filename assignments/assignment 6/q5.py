input_string=input("enter string: ")
words=input_string.split("-")
words.sort()
def convert(lst):
    return '-'.join(lst)

print(convert(words))