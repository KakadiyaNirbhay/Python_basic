# for i in range(1,5,1):
#     for x in range(5,0,i):
#         print(x,end="")
#     print("")

# print("\nWelcome to the guessing game 2.0")
# print("Example for Stack Overflow!\n")

# # ____A____
# # ___B_B___
# # __C___C__
# # _D_____D_
# # E_E_E_E_E


# n = 5
# alph = 65
# for i in range(0, n):
#     print("_" * (n-i), end="_")
#     for j in range(0, i+1):
#         if j==0 or j==i+1 or i==n-1 :
#             print(chr(alph), end="_")
#             alph += 1
         
#     alph = 65
#     print("_")


# for i in range(0,5+1):
#     for j in range(2*i+1):
#         print(chr(65 + i), end=" ")
#     print()

# import random
# number = random.randint(1, 100)
# tries = 0

# for tries in range(5):
#     guess = int(input("Guess a number: "))
#     tries += 1

#     if guess == number and tries <= 10:
#         print("\nCongratulations! You've guessed it in", tries, "tries!")
#         break
#     elif guess < number and tries < 10: 
#         print("Higher...")
#         tries += 1
#     elif guess > number and tries < 10:
#         print("Lower...")
#         tries += 1
#     elif tries >= 11:
#         print("\nI'm afraid to haven't got any tries left. You've exceeded the limit.")

# rows = int(input("Enter the number of rows: "))
# for i in range(rows):
#     if i % 3 == 0:
#         print("* * *")  
#     else:
#         print("  *  ")  

# i = 5  
# while True:
#     print(f"Current value of i: {i}")
#     i -= 1  
#     if i > 0:
#         break  
# print("Exited the loop.")


# divisor = int(input("Enter a number to check divisibility (divisor): "))

# while True:
    
#     number = int(input("Enter a number to check for divisibility (or enter 0 to quit): "))
    
#     if number == 0:
#         print("Exiting the program.")
#         break
    
#     if number % divisor == 0:
#         print(f"{number} is divisible by {divisor}.")
#     else:
#         print(f"{number} is not divisible by {divisor}.")

# MAX_VALUE = 10
# number = int(input(f"Enter a number (0 to {MAX_VALUE}) to calculate its factorial: "))

# if number < 0 or number > MAX_VALUE:
#     print(f"Please enter a number between 0 and {MAX_VALUE}.")
# else:
#     factorial = 1
#     count = 1

#     while count <= number:
#         factorial *= count
#         count += 1

#     print(f"The factorial of {number} is {factorial}.")


lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)