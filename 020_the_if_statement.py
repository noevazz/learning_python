# the if statement allow us to execute an specific code only if boolean expresion is True:
#if boolean_expresion:  <-- note that ":" are required at the end
#    Execute this core  <-- Note code inside the if statement has 4 spaces (or a tab) at the begginig
# ---> We need to place al the code inside (4 spaces at the begining)

pepsi = 6

if pepsi < 8:
    print("yeah I will buy it")

# there is also a structure that allow us to execute code if the boolean expresion is False:
my_money = 9
fanta = 10
if my_money >= fanta:
    print("yeah I have enough money")
else:
   print("nope, I need more money :(")

# AND also there is a structure to do multiple comparations, only one of them will be executed the rest will be ignored:
user_color = "black"
if user_color == "red":
    print("your color is red")
elif user_color == "green":
    print("your color is greeen")
elif user_color == "white":
   print("your color is white")
else:
   print("well I don't know")

# NOTE, when using elif the final else is optional

# you can nest if statemenets:

money = 100
pepsi = 50
fanta = 60
if money > 90:
    if pepsi+fanta <= money:
        print("I will have both")
    elif pepsi <= money:
        print("I don't have money for both, but give me a pepsi")
    elif fanta <= money:
        print("I don't have money for both neither just one pepsi but give me one fanta")
    else:
        print("I do not have enough money")
else:
    print("I have money but I will just keep it for now")


# FINALLY
# the if/elif/elses structures can have a special piece of code called pass:
if True:
    pass # pass doesn't mean anything but you can put it when you don' have something to put inside, this is because all if/elif/else structures required something inside
