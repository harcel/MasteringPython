# Assignment 1
a = 1
b = 2
a, b = b, a
print(a, b)

######################################## Cut cells here.

# Assignment 2
my_list = [1, 2, 3, 4, 50, 60]
first, *other, last = my_list
print(first)
print(other)
print(last)

######################################## Cut cells here.

#Assignment 3
x = [[31,17],
[40 ,51],
[13 ,12]]
print(list(zip(*x)))

######################################## Cut cells here.

# Assignment 4
import string
caesar = {i:a for i, a in enumerate(string.ascii_lowercase)}
def decrypt(shift, cipher): 
    deciphered = [caesar[(string.ascii_lowercase.index(k)-shift)%26] for k in cipher]
    return "".join(deciphered)

for shift in range(1, 26):
    print(f'{shift:2.0f}: {decrypt(shift, "zvsbapvu")}')
# A shift of 7 seems most likely
