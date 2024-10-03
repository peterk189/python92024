#task 2
# true and false 
# not true or false true and not false
# not true or not false
# not true and not false


#Task 3
# A programm to demostrate the single if statement
import random


number = random.randint(1,10)


guess = int(input("Enter a number between 1-10: "))


if guess == number:
    print("Your guess was right!")
    print("WElll done")
    
    
    print ("Goodbye")
    
else: print("Unlucky try again")

