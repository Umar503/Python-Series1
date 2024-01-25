def generator():
    
    i = 1
    while i<=100:
        yield i
    
        i += 1
print(generator())
g = generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))