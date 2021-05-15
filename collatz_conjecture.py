""" Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes
to reach one using the following process: If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1. """

number  = int(input("Enter any number greater than 1: "))
count = 0
while(number != 1):
    temp_num = number%2
    if(temp_num == 0):
        number= number/2
        count=count+1
    else:
        number = (number *3)+1
        count+=1

print(count)

