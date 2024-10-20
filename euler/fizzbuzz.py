"""
recebe um num
de um até o numero:
    Se for div. por 3 e por 5, retorna FizzBuzz
    se for só por 3: Fizz
    se só por 5 Buzz
    se N: retorna o numer
"""

def fizz_buzz(n):
    for i in range(1, (n + 1)):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if "__main__" == __name__:
    fizz_buzz(15)
