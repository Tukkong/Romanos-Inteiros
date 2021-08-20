
print('''Escolha uma conversão até 3999: 
 [ 1 ] Romanos 
 [ 2 ] Decimais''')

opção = int(input("Digite sua escolha: "))


if opção == 1:
     num = int(input("Digite um número inteiro: "))
    
else:
     opção == 2
     letra = input("Digite um Algarismo Romano: ")

#função converter inteiro em romano
def trans_romano(num):
        if(num == 1): return "I"
        if(num == 4): return "IV"
        if(num == 5): return "V"
        if(num == 9):  return "IX"
        if(num == 10): return "X"
        if(num == 40): return "XL"
        if(num == 50): return "L"
        if(num == 90): return "XC"
        if(num == 100): return "C"
        if(num == 400): return "CD"
        if(num == 500): return "D"                         
        if(num == 900): return "CM"
        if(num == 1000): return "M"        
#loop for encadeado decompõem num em milhar, centena, dezena e unidade, retornando de acorda com os Ifs.
        for i in [1000, 100, 10, 1]:            
            for j in [9*i, 5*i, 4*i, i]:
                if(num>=j):
                    return trans_romano(j) + trans_romano(num-j)

if opção == 1:              
      print(trans_romano(num)) 


#função converter número romano em decimal 
def trans_decimal (letra):
     valor = {"I":1 , "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
     soma = 0
     aAnterior = 0
#loop for faz a leitura de traz pra frente, de cada caractere, e guarda na variável. Conferindo com o array, somando ou subtraindo.    
     for item in reversed(letra):
          valorAtual = valor[item]
          
          if (valorAtual >= aAnterior):
               soma += valorAtual
          else:
                soma -= valorAtual
                   
          aAnterior = valorAtual    
     return soma

try:              
     if opção == 2:
          print(trans_decimal(letra))  

except KeyError:
     print(trans_decimal(letra.upper()))