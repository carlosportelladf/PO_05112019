#informa o nome da pessoa
pessoaNome = input ("informe o nome da criatura: ")
#informa o primeiro valor
a = input("informe o primeiro valor: ")
#informa o segundo valor
b = input("informe o segundo valor: ")

# efetua a soma das variaveis
soma = a + b
# testes para mostrar o resultado
if (soma > a):  #caso a soma seja maior do que a variavel a
    print (pessoaNome + ", a soma eh maior que o primeiro valor")
elif(soma == a): #caso a soma seja igual do que a variavel a
    print (pessoaNome +  ", a soma eh igual ao primeiro valor")
else: #caso a soma seja menor do que a variavel a
    print (pessoaNome +  ", a soma eh menor que o primeiro valor")
# trabalhando com strings    
print ("-a primeira letra do nome eh ", pessoaNome[0])
print ("-a segunda letra do nome eh ", pessoaNome[1])
#Funcao len indica o tamanho da string
# subtrai um pois começa do zero
print ("-a ultima letra do nome eh ", pessoaNome[len(pessoaNome) - 1 ])
