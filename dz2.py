def type_logger(callback):
    def wrapper(*args, **kwargs):

        key = callback.__name__
        type_args = type(*args)
        area = f'{key}{*args, type_args}'

        return area
    return wrapper


@type_logger
def cal_cube(x):
    return x ** 3

a = cal_cube(5)
print(a)

