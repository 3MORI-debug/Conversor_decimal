decimal = int(input("Digite um numero decimal: "))
selec = str(input("Selecione a conversão: \nBinario - B\n Octadecimal - O\nHexaDecimal - H\n :"))


if selec == "B" or selec == "b":
    binario = "" ##variavel string vazia para armazenar o valor da conversão

    while decimal > 0: #looping para repetir o calculo ate que o valor "zere"
        resto = decimal % 2 #resto da divisão
        binario = str(resto) + binario ##constroi o resultado acrescentando o proximo valor sempre a esquerda
        decimal = decimal // 2 #divide o numero decimal atual resultando na parte inteira do calculo, sem considerar os valores apos a virgula
    print(binario) #imprime o resultado

elif selec == "O" or selec == "o":
    octadecimal = ""

    while decimal > 0:
        resto = decimal % 8
        octadecimal = str(resto) + octadecimal
        decimal = decimal // 8
    print(octadecimal)

elif selec == "H" or selec == "h":
    hexadecimal = ""

    while decimal > 0:
        resto = decimal % 16
        hexadecimal = str(resto) + hexadecimal
        decimal = decimal // 16
    print(hexadecimal)
elif selec != "B" or selec != "b" or selec != "O" or selec != "o" or selec != "H" or selec != "h":
    print("valor invalido!")