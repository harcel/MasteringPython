def cache_this(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args not in cache:
            print(f"Caching NEW value for {func.__name__}{args}")
            cache[args] = func(*args, **kwargs)
        else:
            print(f"Using OLD value for {func.__name__}{args}")

        return cache[args]
    return wrapper


@cache_this
def add(a, b):
    print("Running add!")
    return a + b

@cache_this
def mul(a, b):
    print("Running mul!")
    return a * b

print(add(3, 7))
print(mul(3, 7))
print(add(3, 7))
print(mul(3, 7))

# Nicer examples could be to check whether some number is prime or other heavy recursive functions. 

# Note, you could also log on disk using pickle, e.g.
