# fibbonacci using generators

def generate_fibbo(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


g = generate_fibbo(5)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
