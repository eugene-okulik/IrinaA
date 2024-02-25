def finish_me_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result

    return wrapper


@finish_me_decorator
def example(text):
    print(text)


example('print me')
