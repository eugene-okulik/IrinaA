def repeat_me(count=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


# Вызываем декорированную функцию
example('print me')


def repeat_me(count=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper if count > 0 else func

    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


# Вызываем декорированную функцию
example('print me')
