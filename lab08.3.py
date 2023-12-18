import requests
import time

def apirequestclosure(url):
    def makerequest():
        response = requests.get(url)
        return response.text
    return makerequest

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

@rate_limit(1)  # Ограничение на 1 вызов в секунду
def getdogfact():
    return apirequestclosure("https://dogapi.dog/api/v2/facts")()

dogfact = getdogfact()
print(dogfact)