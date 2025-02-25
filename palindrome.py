# pede pro usuário digitar algo
texto = input("Type something: ")

# inverte o texto do usuário
otxet = texto[::-1]

# se o texto foi igual normal e ao contrário falar que é um palindromo, caso contrário falar que não é 
if texto == otxet:
    print("It is a palindrome!!!\n")
else:
    print("It's not a palindrome.\n")
