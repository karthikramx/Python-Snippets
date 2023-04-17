# range is a generator
import time

print(range(100))
print(len(range(100)))
print(len(list(range(100))))


def measure_time(func):
    def wrap_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"The function took: {end-start} seconds")
    return wrap_func


@measure_time
def generator_func():
    for i in range(10000000):
        i * i

@measure_time
def not_generator_func():
    for i in list(range(10000000)):
        i * i


generator_func()
not_generator_func()


