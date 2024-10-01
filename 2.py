# x=[1,2,[4,5,6],7,8,[9,[3,5,6],7]]
# print(x[5][1][1])

# x=[1,2,[3,4],[5,6,7],[1,2,[3,4,[5,6]]]]
# print(x[4][2][2][0])

# for i in range(1,5+1):
#     print(" "*(5-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("") 
# for i in range(5 - 1, 0, -1):
#     print(" "*(5 - i),end=" ")
#     for j in range(1, i + 1):
#         print(j,end=" ")
#     print(" ")   

# for i in range(1,6):
#     print(' '*(5-i),end="")
#     print("* " * i)
         
# for i in range(4,0,-1):
#     print(' '*(5-i),end="")
#     print("* " * i) 
       
# for i in range(1,6):
#     print(' '*(5-i),end="")
#     print("* " * i) 
# for i in range(4,0,-1):
#     print(' '*(5-i),end="")
#     print("* " * i)     

# for i in range(5):
#     for j in range(i + 1): 
#         print(10 - j * 2, end=" ")
#     print()  

# for i in range(5):
#     for j in range(i + 1): 
#         print(2*i+1, end=" ")
#     print()  

# for i in range(5):
#     char = chr(69 - i) 
#     for j in range(5 - i):
#         print(char, end="")
#     print("")  
    
# n = int(input("Enter a number:-> "))
# s = 0
# t = n
# while t > 0:
#    digit = t % 10
#    s += digit ** 3
#    t //= 10
# if n == s:
#    print(n,"Armstrong")
# else:
#    print(n,"not Armstrong")
    
# for i in range(4):
#     char = chr(95) 
#     for j in range(5):
#         print(char, end="")
#     print("")  
    
# for i in range(6):
#     char = chr(64)
#     print(char * (i))

# for i in range(1,5+1):
#     char=chr(35)
#     print(" "*(5-i),end=" ")
#     for j in range(1,i+1):
#         print(char,end=" ")
#     print("") 

# print("\nWelcome to the guessing game 2.0")
# print("Example for Stack Overflow!\n")

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

# n = 10
# number = int(input(f"Enter a number (0 to {n}) to calculate its factorial: "))
# if number < 0 or number > n:
#     print(f"Please enter a number between 0 and {n}.")
# else:
#     factorial = 1
#     count = 1
#     while count <= number:
#         factorial *= count
#         count += 1
#     print(f"The factorial of {number} is {factorial}.")

# lower = 0
# upper = 100
# print("Prime numbers between", lower, "and", upper, "are:")
# for num in range(lower, upper + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# word = input("Enter a word: ")
# word = word.lower()
# if word == word[::-1]:
#     print(word, "palindrome")
# else:
#     print(word, "not palindrome")

# for  i in range(1,6):
#     for j in range(i,6):
#         print(j,end="")
#     print("")

# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j,end="")
#     print()

