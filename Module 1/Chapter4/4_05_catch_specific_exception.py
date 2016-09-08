def funny_division(anumber):
    try:
        return 100 / anumber
    except ZeroDivisionError:
        return "Silly wabbit, you can't divide by zero!"

print(funny_division(0))
print(funny_division(50.0))
print(funny_division("hello"))
