# define a function that generates the Fibonacci series
def fibonacci(n):
    # initialize the first two numbers in the series
    a, b = 0, 1

    # generate the Fibonacci series
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

        print()  # add a newline after the series


#after this create a new python file and import this file and implement the above line
# generate the first 10 numbers in the series
fibonacci(int(input("Enter num: ")))
