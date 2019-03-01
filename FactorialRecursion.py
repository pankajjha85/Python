# An example of a recursive function to
# find the factorial of a number

def CalculateFactorial(prm_input):
    """This is a recursive function
    to find the factorial of an integer"""

    if prm_input == 1:
        return 1
    else:
        return (prm_input * CalculateFactorial(prm_input-1))

num = int(input('Please enter the number to calculate the Factorial.'))
print("The Factorial of", num, "is", CalculateFactorial(num))