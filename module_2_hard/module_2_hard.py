import random
def generate_password():
    numbers = list(range(3, 20))
    n = random.choice(numbers)
    result = ""
    for i in range(1, n):
        for j in (range(i, n)):
            if i == j:
                continue
            elif n % (i + j) == 0:
                result += str(i) + str(j)
    print(n)
    print(result)
generate_password()
