def with_previous(iterable):
    """Yield (previous, current) tuples, 
    starting from second
    """
    iterator = iter(iterable)
    previous = next(iterator)
    for item in iterator:
        yield previous, item
        previous = item

differences = [current-previous for previous, current in with_previous(my_list)]

print(differences)
