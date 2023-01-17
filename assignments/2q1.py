statement="Python is a case sensitive language"
print(len(statement))
reversedString=statement[len(statement)::-1]
print(reversedString)
newString=statement[10:26]
print(newString)
replacedString= statement.replace("a case sensitive", "object oriented")
print(replacedString)
letter="a"
print(statement.find(letter))
no_white_spaces=statement.replace(" ", "")
print(no_white_spaces)