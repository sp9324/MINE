inputString = str(input("enter string: "))

length = len(inputString)

count = 0

for i in range(0, length):
    if inputString[i] == " ":
        count += 1

wordsCount = count+1

if wordsCount != 1:
    print(wordsCount)
else:
    print(length)
