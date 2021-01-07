def validacao_idade(idade):
    if idade>=18:
        print(f'\nVocê possui idade suficente para dirigir. Vamos prosseguir, {nome}.\n')
        return True
    else:
        print(f' {nome}, infelizmente você não possui idade suficiente para dirigir.')
        return False
    
def escolha_carteira():
    print('Escolha uma das opções abaixo:')
    print('1 - Carro\n2 - Moto\n3- Carro e Moto')
    return int(input())

def calculo_preco(escolha):
    valor_carro = 1500
    valor_moto = 1000
    
    if escolha == 1:
        return valor_carro
    elif escolha == 2:
        return valor_moto
    else:
        return valor_carro + valor_moto
    

def interessado():
    print('Está interessado(a)?')
    print('1-Sim\n2-Não')
    interesse = int(input())
    if interesse == 1:
        return True
    else:
        return False
        
def desconto(valor):
    return valor - (valor*0.1)

    
nome = input('Digite seu nome, por favor: ')
idade = int(input('Digite sua idade, por favor: '))

if validacao_idade(idade):
    escolha = escolha_carteira()
    
    valor = calculo_preco(escolha)
    print(f'{nome}, o valor total ficou em {valor} reais.')
    
    if interessado():
        print('Perfeito! Começaremos amanhã!')
    else:
        print('Posso conversar com o gerente e checar a possibilidade de um desconto...')
        valor = desconto(valor)
        print(f'Com desconto, consigo fazer por {valor} reais.')
        if interessado():
             print('Perfeito! Começaremos amanhã!')
        else:
             print('Tudo bem, me avise se mudar de ideia!')
            