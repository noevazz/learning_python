try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())

"""
without "trying" the code:
i = int("Hello!")

this will raise a ValueError exception
ValueError: invalid literal for int() with base 10: 'Hello!'

In "except Exception as e" e is equals to "invalid literal for int() with base 10: 'Hello!'"

"""