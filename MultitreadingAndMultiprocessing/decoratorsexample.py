# Functions that modifies another function
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__!r} took "
              f"{time.time() - start_time:.4f} sec to execute.")
        return result
    return wrapper

@timer
def example_function(n):
    return f"The sum of the numbers is {sum(range(n))}"

print(example_function(2000))