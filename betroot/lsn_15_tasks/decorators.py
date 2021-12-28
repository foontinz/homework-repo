def logger(function):
    def wrapper(*args):
        print(function.__name__)
        print(*args)
        function(*args)
    return wrapper


@logger
def add(*args):
    return sum(args)


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(3,1)
square_all(312,3123,12,123,13,23)