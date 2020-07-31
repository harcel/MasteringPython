import time
import datetime

def logtime(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time

        with open('timelog.txt', 'a') as outfile:
            outfile.write(f'{datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")}: '
                          f'{func.__name__}. Run time: {total_time}\n')
        return result

    return wrapper


@logtime
def slow_add(a, b):
    time.sleep(2)
    return a + b

@logtime
def slow_mul(a, b):
    time.sleep(3)
    return a * b

# Example file will be created - Subsequent use will append to the file
for i in range(5):
    for j in range(5):
        print(slow_add(i, j))
        print(slow_mul(i, j))

