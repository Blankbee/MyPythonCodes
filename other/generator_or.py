def fibonacci(c):
    a=1
    b=1
    print(a)
    print(b)
    for i in range(0,c):
        a, b=b, b+a
        yield b

for j in fibonacci(6):
    print(j)

