import time

def rate_limit(limitpersecond):
    def decorator(func):
        last_called = 0

        def wrapper(*args, **kwargs):
            nonlocal last_called
            elapsed = time.time() - last_called
            if elapsed < 1 / limitpersecond:
                time.sleep(1 / limitpersecond - elapsed)
            last_called = time.time()
            return func(*args, **kwargs)

        return wrapper

    return decorator

@rate_limit(2)  # Ограничение на 2 вызова в секунду
def my_function():
    print("Вызвана функция my_function")

my_function()
time.sleep(0.5)
my_function()
my_function()