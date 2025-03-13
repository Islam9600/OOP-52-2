# hw4.py

def to_uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@to_uppercase
def greet(name):
    return f"Привет, {name}!"

@to_uppercase
def say_hello():
    return "Привет!"

print(greet("Мир"))
print(say_hello())
