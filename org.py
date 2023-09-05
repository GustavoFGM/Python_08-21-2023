#Aula python 08/21/2023
'''
ExercÃ­cio 18:  ConcatenaÃ§Ã£o de Strings

Crie uma funÃ§Ã£o que recebe strings para serem concatenadas
'''

#Definicao de funÃ§Ã£o

def concatena_strings(*args):
    return ''.join(args)

strings = input("Digite uma lista de strings separadas por espaÃ§o: ").split()
resultado = concatena_strings(*strings)
print(f"A concatenaÃ§Ã£o das strings Ã©: {resultado}")

'''
ExercÃ­cio 19:  Contagem de Vogais

Crie uma funÃ§Ã£o que faÃ§a contagem de vogais.
lembre-se que o Python Ã© Case sensitive
'''

#Definicao de funÃ§Ã£o

def conta_vogais(*args):
    vogais = 'aeiouAEIOU'
    count = 0
    for arg in args:
        count += sum(1 for char in arg if char in vogais)
    return count

strings = input("Digite uma lista de strings separadas por espaÃ§o: ").split()
resultado = conta_vogais(*strings)
print(f"Total de vogais: {resultado}")


'''
ExercÃ­cio 20: Calculadora de Desconto

Crie uma funÃ§Ã£o para criar uma calculadora para calculo de desconto

'''

#Definicao de funÃ§Ã£o

def calcula_desconto(**kwargs):
    total = kwargs.get('total', 0)
    desconto = kwargs.get('desconto', 0.1)
    valor_com_desconto = total * (1 - desconto)
    return valor_com_desconto

total = float(input("Digite o valor total: "))
desconto = float(input("Digite a taxa de desconto (em decimal): "))
resultado = calcula_desconto(total=total, desconto=desconto)
print(f"Total com desconto: {resultado}")


'''
ExercÃ­cio 21: OrdenaÃ§Ã£o de NÃºmeros

Crie uma funÃ§Ã£o que ordene uma lista de numeros

'''

#Definicao de funÃ§Ã£o

def ordena_numeros(*args):
    return sorted(args)

numeros = [float(x) for x in input("Digite uma lista de nÃºmeros separados por espaÃ§o: ").split()]
resultado = ordena_numeros(*numeros)
print(f"NÃºmeros ordenados: {resultado}")


'''
ExercÃ­cio 22: ConversÃ£o de Unidades

Crie uma funÃ§Ã£o que converta de centimentos para metros e de metros
para centimentos respectivamente

'''

#Definicao de funÃ§Ã£o

def converte_unidades(**kwargs):
    valor = kwargs.get('valor', 0)
    unidade = kwargs.get('unidade', 'cm')

    if unidade == 'cm':
        return f"{valor} cm Ã© igual a {valor * 0.01} m"
    elif unidade == 'm':
        return f"{valor} m Ã© igual a {valor * 100} cm"

valor = float(input("Digite o valor: "))
unidade = input("Digite a unidade (cm/m): ")
resultado = converte_unidades(valor=valor, unidade=unidade)
print(resultado)


'''
ExercÃ­cio 23:  Lista de Compras

Crie uma funÃ§Ã£o que crie uma  Lista de Compras

'''

#Definicao de funÃ§Ã£o

def lista_de_compras(**kwargs):
    itens = kwargs.get('itens', [])
    return itens

itens = input("Digite uma lista de itens de compra separados por espaÃ§o: ").split()
compras = lista_de_compras(itens=itens)
print(f"Lista de compras: {compras}")


'''
ExercÃ­cio 24:   Contagem de args

Escreva uma funÃ§Ã£o que conte e retorne quantos argumentos foram passados para ela.

'''

#Definicao de funÃ§Ã£o

def contar_args(*args):
    return len(args)

numeros = input("Digite nÃºmeros separados por espaÃ§o: ").split()
resultado = contar_args(*numeros)
print("Total de argumentos:", resultado)


'''
ExercÃ­cio 25:   FunÃ§Ã£o com kwargs para informaÃ§Ãµes de usuÃ¡rio

Crie uma funÃ§Ã£o que receba informaÃ§Ãµes de usuÃ¡rio (nome, idade, cidade) 
como argumentos nomeados e imprima-as.

'''

#Definicao de funÃ§Ã£o

def info_usuario(**kwargs):
    print("Nome:", kwargs.get('nome'))
    print("Idade:", kwargs.get('idade'))
    print("Cidade:", kwargs.get('cidade'))

info = {
    'nome': input("Nome: "),
    'idade': input("Idade: "),
    'cidade': input("Cidade: ")
}
info_usuario(**info)

'''
ExercÃ­cio 26:   FunÃ§Ã£o com *args e kwargs para saudaÃ§Ãµes
Crie uma funÃ§Ã£o que aceite o nome do usuÃ¡rio como argumento posicional (*args) 
e outras informaÃ§Ãµes como argumentos nomeados (**kwargs) para gerar
saudaÃ§Ãµes personalizadas.

'''

#Definicao de funÃ§Ã£o

def saudacao_personalizada(*args, **kwargs):
    nome = args[0]
    saudacao = kwargs.get('saudacao', 'OlÃ¡')
    sobrenome = kwargs.get('sobrenome', '')
    idade = kwargs.get('idade', '')
    print(f"{saudacao}, {nome} {sobrenome}! {idade}")

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = input("Idade: ")
saudacao_personalizada(nome, saudacao="Oi", sobrenome=sobrenome, idade=idade)

