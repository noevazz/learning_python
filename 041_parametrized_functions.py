# functions can have arguments with default values
# it means that if you invoke the function without providing that argument the function will ise the default value:
def greeting(first_name, last_name="Vazquez"):
    print("hi mi name is", first_name, last_name)

greeting("Noe")
greeting("Andy", "Contreras")