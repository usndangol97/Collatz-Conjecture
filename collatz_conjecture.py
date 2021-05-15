""" Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes
to reach one using the following process: If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1. """

number  = int(input("Enter any number greater than 1: "))
count = 0
while(number != 1):
    temp_num = number%2
    if(temp_num == 0):
        test_num = number
        number= number/2
        count=count+1
        print("{} / 2 = {}".format(test_num,number))
    else:
        test_num = number
        number = (number *3)+1
        count+=1
        print("({}* 3 )+1 = {}".format(test_num, number))

print("Number of steps taken : {}".format(count))

