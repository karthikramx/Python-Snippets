is_old = False
is_licensed = True

if is_old and is_licensed:
    print('You are old enough to drive')
elif is_licensed: # only runs if the pervious condition evals to false and the current conditions runs if its true
    print('You can drive now')
else: # only runs if the if condition evals to false
    print('You are not old enough to drive')


