cube = lambda x: x * x * x

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = []
    for i in range(n):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            newn = fib[i - 2] + fib[i - 1]
            fib.append(newn)
    return fib
                        
if __name__ == '__main__':
    n = int(input("Enter fibonacci length to be cubed: "))
    print(list(map(cube, fibonacci(n))))