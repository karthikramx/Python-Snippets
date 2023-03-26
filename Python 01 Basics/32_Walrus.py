# the freaking walrus operator

a = 'hellllloooooooooooo'
while (n := len(a)) > 10:
    print(f"the length is {n}")
    a = a[:-1]