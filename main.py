'''
Calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes infromações: 
Rendimento, altura e largura.
'''

rendimento = int(input('Qual é o rendimento da lata? '))
altura = int(input('Qual é a altura da parede? '))
largura = int(input('Qual é a largura da parede? '))

# calculo: altura x largura / rendimento = x latas
def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()