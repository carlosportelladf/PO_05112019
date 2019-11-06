pessoaNome = "Portella"
a = 1
b = -1

# efetua a soma das variaveis
soma = a + b
# testes para mostrar o resultado
if (soma > a):  #caso a soma seja maior do que a variavel a
    print (pessoaNome + ", a soma eh maior que a")
elif(soma == a): #caso a soma seja igual do que a variavel a
    print (pessoaNome +  ", a soma eh igual a a")
else: #caso a soma seja menor do que a variavel a
    print (pessoaNome +  ", a soma eh menor que a")
# trabalhando com strings    
print ("a primeira letra do nome eh ", pessoaNome[0])
print ("a segunda letra do nome eh ", pessoaNome[1])
#Funcao len indica o tamanho da string
# subtrai um pois começa do zero
print ("a ultima letra do nome eh ", pessoaNome[len(pessoaNome) - 1 ])
