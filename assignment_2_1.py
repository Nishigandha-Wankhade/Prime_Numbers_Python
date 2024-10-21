"""
-----------------------------------------------------------------------
Assignment 2_1: Searching 450th Prime Number .
September 25, 2024 
Nishigandha Wankhade 
-----------------------------------------------------------------------
"""
# execute (pip install colorama) in command prompt and
# execute (pip install termcolor) too
import math
#from colorama import Fore, Style, init

# function to find number is prime number or not
def prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# function to find 450th prime number
def find_450th_prime():
    count = 0
    number = 1
    list1 = []
    while count < 450:
        number += 1
        if prime(number):
            count +=1
            list1.append(number)
            #printing prime numbers after every 50 primes
            if count % 50 == 0:
                print(f"{count} prime numbers found so far")
                #print(f"{Fore.YELLOW}{count} prime numbers found so far")
    
    print("\t\t\n\t\t===========*****  The 450th Prime Number is ", number, " *****===========")
    print("\n\n All ", count, " prime numbers are: \n", list1)
    #print(f"{Fore.GREEN}\t\t\n\t\t===========*****  The 450th Prime Number is ", f"{Fore.RED}{number}", f"{Fore.GREEN} *****===========")
    #print(f"{Fore.CYAN}\n\n All ", count, " prime numbers are: \n", list1)


# calling function find_450th_prime()
find_450th_prime()