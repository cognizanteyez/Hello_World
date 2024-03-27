fruits = ["apple", "banana", "pear", "blueberry", "raspberry"]

for i in fruits:
    index = fruits.index(i)
    if i[-1] == "y":
        fruits[index] = i[0:-1] + "ies"
    else:
        fruits[index] = i + "s"


print(fruits)