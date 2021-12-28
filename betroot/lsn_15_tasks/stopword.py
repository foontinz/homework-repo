from functools import wraps


def stop_words_filter(words: list):
    def filter(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            rez = function(*args, *kwargs)
            for word in words:
                if word in rez:
                    rez = rez.replace(word, '*')
            return rez

        return wrapper

    return filter


@stop_words_filter(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


