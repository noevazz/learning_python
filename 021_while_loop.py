# loops allow us to execute code several times while a boolean expression is True or while we do not break the loop explicit

# while loop:

money = 0
fanta = 43

while money < fanta:
   #save 11 dollar each day to buy a fanta
    money += 11
    print("I have", money, "dollars")

# there is also inifinite loops:

money_in_bank = 12
while True:
    deposit = float(input("enter deposit: "))
    money_in_bank += deposit
    if money_in_bank > 100:
        print("you already have more thatn 100 dollars")
        break # break the loop right now
print("\nlet's go to the next exercise\n")

# loops can have an else estatement, it will execute its code at the end of the loop,
# but if the loop is broke (using break) the else code is not executed
control_loop = True
while control_loop:
    option = input("you are in a loop, insert your option \n[break: exit using break, normal: exit normally]: ")
    if option == "break":
        print("Ok let's break the loop")
        break # the else is not going to be executed
    elif option == "normal":
        print("Ok let's stop the loop normally")
        control_loop = False # ends the loop normally, the else will be executed
    else:
        print("continuing...")
else:
    print("Hi from the else statement")

print("\nLet's go to the next exercise:\n")
print(":D")
# Note: rember you can use the pass structure if you don't have a specific code to put inside a if/elif/else and also a while:
#while True:
    #pass   <-- but this will cause the program to be stuck doing nothing

# FINALLY: the continue structure
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
number = 10
while number >= 0:
    if number%2 == 0:
        number -= 1
        continue
    print("I have a lot of code to execute but only if", number, "is an odd number, an yes it is")
    number -= 1
else:
    print("end of the loop")
