user_input = input('Enter space-separated integers: ')

my_tuple = tuple(int(item) for item in user_input.split())

for item in my_tuple:
    print("(", item, ",", item*item, ")")
