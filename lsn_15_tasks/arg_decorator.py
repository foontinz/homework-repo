def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            words = ''.join(contains)
            if words in result or len(result) < max_length or type(result) != type_:
                return False
            return result

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
print(create_slogan('S@SH05'))
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
