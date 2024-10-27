def calculadora():
    while True:
     entrada = input('digite o operador ')
    
     try:
      numero = int(input('digite um numero '))
      outro_numero = int((input('digite outro numero ')))
      if entrada == 'somar':
        print(numero + outro_numero)
      elif entrada == 'diminuir':
        print(numero - outro_numero) 
      elif entrada == 'dividir':
        print(numero / outro_numero)
      elif entrada == 'multiplicar':
        print(numero * outro_numero)  
      else:
        print('erro! ')   
     except:
       print('digite apenas numeros!')       
               


calculadora()            
