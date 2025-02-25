# Testar se é armstrong
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number

# Output pro usuário
num = int(input("Type a number: "))
if is_armstrong(num):
    print(f"{num} It is an armstrong number!")
else:
    print(f"{num} It's not an armstrong number.")
