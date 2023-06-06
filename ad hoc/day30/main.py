fruits = ["Apple", "pear", "Orange"]


# TODO: Catch the exception and make sure the code runs
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        fruit = "Fruit"
    print(fruit + " pie")


make_pie(4)
