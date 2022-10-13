from math import sqrt

"""List of prime numbers generator."""

def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError("ValueError exception thrown")
    list = []
    temp = 0
    while (number_of_primes != 0):
        check = True
        if (temp>1):
            #check from 2 to the square root of temp - prime in only those circumstances
            for i in range(2, int(sqrt(temp))+1):
                if (temp % i == 0):
                    check = False
            #if temp is prime, add it to list
            if (check == True):
                list.append(temp)
                number_of_primes = number_of_primes - 1
        check=False
        temp = temp + 1

    return list
