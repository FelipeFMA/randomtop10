# Testar se é armstrong
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number

# Output pro usuário
num = int(input("Digite um número: "))
if is_armstrong(num):
    print(f"{num} é um número de Armstrong!")
else:
    print(f"{num} não é um número de Armstrong.")
