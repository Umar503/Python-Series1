def decorator(hello):
    def wrapper():
        print("Before calling Hello")
        hello()
        print("After calling Hello")
    return wrapper

@decorator
def hello():
    print("Please Wait")
hello()