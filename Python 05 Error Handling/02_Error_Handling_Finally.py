# Error handling for an input
# using Finally

while True:
    try:
        num = int(input("Please enter your age:"))
        5/num
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Please enter a number greater than zero")
    else:
        print("Thank you, see you soon!")
        break
    finally:
        print("Im finally done with this")