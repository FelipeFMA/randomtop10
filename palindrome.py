# pede pro usuário digitar algo
texto = input("Digite algo: ")

# inverte o texto do usuário
otxet = texto[::-1]

# se o texto foi igual normal e ao contrário falar que é um palindromo, caso contrário falar que não é 
if texto == otxet:
    print("É um palindromo!")
else:
    print("Não é um palindromo")
