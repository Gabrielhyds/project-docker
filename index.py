#Apresentação do sistema
print("Olá, Seja bem-vindo, programa criado para converter temperaturas:\n\nNOME: Gabriel Yoshino RA: 195463\n\n")

#condição que fará o programa parar
continuar = input("Deseja continuar? digite (S)im para continuar ou (C)ancelar: ")

#enquanto o continuar for diferente de c (maiusculo quando minusculo)
while (continuar != "c"):
  
  #apresentando o menu de opções
  print("\n\n1 - (celsius para fahrenheit)\n2 - (fahrenheit para celsius)\n3 - (celsius para kelvin)\n4 - (fahrenheit para kelvin)\n5 - (kelvin para celsius)\n6 - (kelvin para fahrenheit)\n")
  
  #variavel que irá armazenar qual das opções foi digitada
  temp = input("Qual das opções você deseja converter: ")


  if (temp == "1"): # se a opção escolhida for a 1 então
    c = int(input("\nDigite a temperatura em celsius: "))
    f = (c * 9 / 5) + 32

    print("A temperatura convertendo (celsius para fahrenheit) é: " + str(f) +"F°")
    continuar = input("\nDeseja continuar? digite (S)im para continuar ou (C)ancelar: ")
  elif (temp == "2"):
    f = int(input("\nDigite a temperatura em fahrenheit: "))
    c = 5 / 9 * (f - 32)

    print("A temperatura convertendo (fahrenheit para celsius) é: " + str(c) + "C°")
    continuar = input("\nDeseja continuar? digite (S)im para continuar ou (C)ancelar: ")
  elif (temp == "3"):
    c = int(input("\nDigite a temperatura em celsius: "))
    k = c + 273.15

    print("A temperatura convertendo (celsius para kelvin) é: "+ str(k) + "K°")
    continuar = input("\nDeseja continuar? digite (S)im para continuar ou (C)ancelar: ")
  elif (temp == "4"):
    f = int(input("\nDigite a temperatura em fahrenheit: "))
    k = 5 / 9 * (f - 32) + 273.15

    print("A temperatura convertendo (fahrenheit para kelvin) é: "+ str(k) + "K°")
    continuar = input("\nDeseja continuar? digite (S)im para continuar ou (C)ancelar: ")
  elif (temp == "5"):
    k = int(input("\nDigite a temperatura em kelvin: "))
    c = k - 273.15

    print("A temperatura convertendo (kelvin para celsius) é: "+ str(c) + "C°")
    continuar = input("\nDeseja continuar? digite (S)im para continuar ou (C)ancelar: ")
  elif (temp == "6"):
    k = int(input("\nDigite a temperatura em kelvin: "))
    c = 5 / 9 * (k - 273.15) + 32

    print("A temperatura convertendo (kelvin para fahrenheit) é: "+ str(c) + "F°")
    continuar = input("\nDeseja continuar? digite (S)im para continuar ou (C)ancelar: ")
  else:
    print("\nNÚMERO INVALIDO TENTE NOVAMENTE!")
