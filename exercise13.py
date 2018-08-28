# Asks for a desired number of Fibonacci sequence

def my_fib(num):
    x = 1
    a = [1]
    for i in range(1, num):
        a.append(x)
        x = a[i] + a[i -1]
    return a

num = int(input('Enter the number of desired Fibonacci elements: '))
print(my_fib(num))
