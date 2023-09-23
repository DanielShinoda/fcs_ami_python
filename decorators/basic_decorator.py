def deco(func):
    def wrapper():
        print("Wrapper func")
    return wrapper

@deco
def f():
    print("f")

print(f)
f()
