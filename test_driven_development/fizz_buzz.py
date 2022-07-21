"""
Given a positive integer N
 Divisible by 3 → print “Fizz”
 Divisible by 5 → print “Buzz”
 Divisible by 3 and 5 → print “FizzBuzz”
 Otherwise → print N
"""


def fizz_buzz(positive_integer):
    if int(positive_integer) and positive_integer > 0 and positive_integer % 3 == 0 and positive_integer % 5 != 0:
        return "Fizz"
    if int(positive_integer) and positive_integer > 0 and positive_integer % 5 == 0 and positive_integer % 3 != 0:
        return "Buzz"
    if int(positive_integer) and positive_integer > 0 and positive_integer % 3 == 0 and positive_integer % 5 == 0:
        return "FizzBuzz"
    if int(positive_integer) and positive_integer > 0 and positive_integer % 3 != 0 and positive_integer % 5 != 0:
        return positive_integer
    else:
        return "Input must be positive integer"
