def funky_for_loop(iterable, action_to_do):
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            action_to_do(item)

funky_for_loop(numbers, print)

# NOTE THE USE OF ELSE. THAT ALSO WORKS IN FOR LOOPS!