# Error handling for an input

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

def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)
    
print(sum('1',2))
