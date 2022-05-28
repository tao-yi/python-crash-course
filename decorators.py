import functools


def my_decorator(prefix: str):
    def outer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix} Something is happening before the function is called.")
            res = func(*args, **kwargs)
            print(f"{prefix} Something is happening after the function is called.")
            return res
        return wrapper
    return outer


@my_decorator(prefix='hello')
def say_whee():
    print("Whee!")


d = my_decorator('hello')(say_whee)
d()

say_whee()
