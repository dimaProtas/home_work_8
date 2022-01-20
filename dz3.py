from functools import wraps


def val_checker(callback):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                if not callback(arg):
                    raise ValueError(f'неправильный аргумент {arg}')
            return func(*args)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-5)
print(a)


