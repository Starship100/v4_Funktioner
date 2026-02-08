"""""
# Läsa och förstå kod

# 1a.
# Guess: Tror ingenting skrivs ut.
def foo(t):
    print("test")

foo("hej")  # test

# 1b
# Guess: 15 (Missade att det var 'print' !!!)
def fun1(x, y):
    return x * y

print(3, 5)  # 3 5

# 1c
# Guess: 15
def fun1(x, y):
    return x * y

print(fun1(3, 5))  # 15

# 1d
# Guess: 10
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))  # Först räknas det inom parantesen x * 5, y * 5 = 10 + 15 = 25
print(a)  # 125 - Sedan räknas den övre funktionen ut 5 * 25

# 1e
# Guess: 7
a = 5
def fun3(a):
    a += 1

a += 2
print(a)  # 7

# 1f
# Guess: 18
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3)
print(a)  # 18

# 1g
def is_number(x):
    if isinstance(x, (str, float, int)):
        return True
    #elif isinstance(x, float):
     #   return True
    return False

print(is_number("hej"))
print(is_number(5.5))
print(is_number(42))
"""""
# 1h
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

print(average_words(["sup", "how's", "it", "going", "reflecting",
              "on", "programs", "and", "coding"]))

# 1i
def find_min(numbers):
    # if numbers == []:
    if not numbers:
        tom_lista = print("Listan är tom.")
        return tom_lista

    counter = numbers[0]
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is:  {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])


