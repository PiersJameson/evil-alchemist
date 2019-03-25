from math import sqrt

def divisors(number):
    divisors = [a for a in range(1,int(number)) if number % a == 0]
    divisors.append(number)
    return divisors