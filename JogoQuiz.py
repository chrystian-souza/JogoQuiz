from time import sleep
import sys


def pergunta1(resposta): # Função criada que levará a resposta a perguntaN1
    if perguntaN1 == 'a' or perguntaN1 == 'A': 
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1 # Vai acrescentar no index 1 o acerto.
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        quiz [0] = quiz [0] -1 # Vai diminuir no index 0 a chance.
        quiz [2] = quiz [2] +1 # Vai acrescentar no index 2 o erro.
        sleep(2)
    return resposta

def pergunta2(resposta):
    if perguntaN2 == 'b' or perguntaN2 == 'B':
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        sleep(2)
    return resposta

def pergunta3(resposta):
    if perguntaN3 == 'c' or perguntaN3 == 'C':
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        sleep(2)
        if quiz [0] == 0: # Condição se o index [0] zerar as chances, ou seja, for igual a 0 o programa encerra.
            print('\033[1;31m''Ops :o, suas chances acabaram, fim do jogo...')
            print('\033[;1m''Resultado:  ')
            print('\033[1;32m'f'Você acertou {quiz[1]} pergunta(s) e errou {quiz[2]}, tente novamente. ')
            print('Fim.')
            sleep(2)
            sys.exit() # Comando para encerrar o programa

    return resposta

def pergunta4(resposta):
    if perguntaN4 == 'b' or perguntaN4 == 'B':
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        sleep(2)
        if quiz [0] == 0:
            print('\033[1;31m''Ops :o, suas chances acabaram, fim do jogo...')
            print('\033[;1m''Resultado: ')
            print('\033[1;323m'f'Você acertou {quiz[1]} pergunta(s) e errou {quiz[2]}, tente novamente. ')
            print('Fim.')
            sleep(2)
            sys.exit()
    return resposta

def pergunta5(resposta):
    if perguntaN5 == 'b' or perguntaN5 == 'B':
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        sleep(2)
        if quiz [0] == 0:
            print('\033[1;31m''Ops :o, suas chances acabaram, fim do jogo...')
            print('\033[;1m''Resultado: ')
            print('\033[1;323m'f'Você acertou {quiz[1]} pergunta(s) e errou {quiz[2]}, chegou na metade ,tente novamente. ')
            print('Fim.')
            sleep(2)
            sys.exit()
    return resposta

def pergunta6(resposta):
    if perguntaN6 == 'b' or perguntaN6 == 'B':
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        sleep(2)
        if quiz [0] == 0:
            print('\033[1;31m''Ops :o, suas chances acabaram, fim do jogo...')
            print('\033[;1m''Resultado: ')
            print('\033[1;323m'f'Você acertou {quiz[1]} pergunta(s) e errou {quiz[2]}, tente novamente. ')
            print('Fim.')
            sleep(2)
            sys.exit()
    return resposta

def pergunta7(resposta):
    if perguntaN7 == 'c' or perguntaN7 == 'C':
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        sleep(3)
        if quiz [0] == 0:
            print('\033[1;31m''Ops :o, suas chances acabaram, fim do jogo...')
            print('\033[;1m''Resultado: ')
            print('\033[1;323m'f'Você acertou {quiz[1]} pergunta(s) e errou {quiz[2]}, tente novamente. ')
            print('Fim.')
            sleep(2)
            sys.exit()
    return resposta

def pergunta8(resposta):
    if perguntaN8 == 'a' or perguntaN8 == 'A':
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        sleep(2)
        if quiz [0] == 0:
            print('\033[1;31m''Ops :o, suas chances acabaram, fim do jogo...')
            print('\033[;1m''Resultado: ')
            print('\033[1;323m'f'Você acertou {quiz[1]} pergunta(s) e errou {quiz[2]}, quase foi, tente novamente. ')
            print('Fim.')
            sleep(2)
            sys.exit()
    return resposta

def pergunta9(resposta):
    if perguntaN9 == 'a' or perguntaN9 == 'A':
        print('\033[1;32m''Você acertou, vamos para a próxima pergunta...\n')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( , vamos para a próxima pergunta...\n')
        sleep(2)
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        if quiz [0] == 0:
            print('\033[1;31m''Ops :o, suas chances acabaram, fim do jogo...')
            print('\033[;1m''Resultado: ')
            print('\033[1;323m'f'Você acertou {quiz[1]} pergunta(s) e errou {quiz[2]},tente novamente. ')
            print('Fim.')
            sleep(2)
            sys.exit()
    return resposta

def pergunta10(resposta):
    if perguntaN10 == 'a' or perguntaN10 == 'A':
        print('\033[1;32m''''Você acertou, essa foi a ultima pergunta. 
\033[;1mResultado... ''')
        quiz [1]= quiz[1] +1
    else:
        print('\033[1;31m''Você errou :( \n')
        quiz [0] = quiz [0] -1 
        quiz [2] = quiz [2] +1
        sleep(2)
        if quiz [0] == 0:
            print('\033[1;31m''Ops :o, suas chances acabaram, fim do jogo...')
            print('Fim.')
            sleep(2)
            sys.exit()
    return resposta


def titulo(texto): # Função titulo que recebe um parâmetro texto
    print(texto)
    print('\033[;1m''-' * 60)
    
    



titulo('\033[1;36m''                  Bєм viηdø αø jøgø Quiz             ')
titulo('\033[1;32m' '* ℝ𝔼𝔾ℝ𝔸𝕊 𝔻𝕆 𝕁𝕆𝔾𝕆 : ')
titulo('\033[1;33m''''- Serão 10 perguntas de temas aleatórios feitas ao jogador.
- O jogador só pode errar 3 vezes durante o jogo.
- Será gerado o resultado de quantas perguntas você acertou e errou.
- BOA SORTE! :)\n''')

quiz = [3,0,0] # [qtdChances, acertos, erros]

while True:

    perguntaN1 = input('\033[;1m''''(1)Quantos planetas Terra cabem dentro do Sol?\n 
a) Um milhão
b) Cem
c) Seiscentos
d) Cento e cinquenta
e) Dois milhões  
                        ''')
    resposta = pergunta1(perguntaN1) # Variável resposta receberá os dados gerados
                                     # pela função pergunta1 recebidos pela resposta do jogador.
    
    perguntaN2 = input('\033[;1m''''Qual das alternativas contém apenas nomes de rios?\n  
a) São Francisco, Douro, Antártico
b) Nilo, Amazonas, Mississipi
c) Cáspio, Vermelho, Reno
d) Tocantins, Bering, Ganges
e) Danúbio, Jordão, Morto
                        ''')
    resposta = pergunta2(perguntaN2)
    
    perguntaN3 = input('\033[;1m''''(3) Em que lugar vivem mais cangurus do que pessoas?\n 
a) Indonésia
b) Nova Zelândia
c) Austrália
d) Papua-Nova Guiné
e) África do Sul
                        ''')
    resposta = pergunta3(perguntaN3) 
    
    perguntaN4 = input('\033[;1m''''(4) Qual a ciência que estuda a atmosfera da Terra e a climatologia?\n
a) Astronomia
b) Metereologia
c) Dispersão atmosférica
d) Meteorologia
e) Horologia 
                        ''')
    resposta = pergunta4(perguntaN4) 
   
    perguntaN5 = input('\033[;1m''''(5)  O etanol é produzido através de qual fonte de energia?\n
a) Solar
b) Biomassa
c) Eólica
d) Geotérmica
e) Hidrelétrica
                        ''')
    resposta = pergunta5(perguntaN5) 
   
    perguntaN6 = input('\033[;1m''''(6) Quantos braços tem um polvo?\n
a) Seis
b) Oito
c) Dez
d) Sete
e) Três 
                        ''')
    resposta = pergunta6(perguntaN6) 
    
    perguntaN7 = input('\033[;1m''''(7) Quantos olhos a maior parte das aranhas têm?\n
a) Dois
b) Quatro
c) Quatro pares
d) Seis
e) Um
                        ''')
    resposta = pergunta7(perguntaN7) 
   
    perguntaN8 = input('\033[;1m''''(8) Nesses pares, ambos são mamíferos:\n
a) Baleia azul e golfinhos
b) Morcegos e galinhas
c) Girafas e tartarugas
d) Porcos e pinguins
e) Macacos e sapos 
                        ''')
    resposta = pergunta8(perguntaN8) 
   
    perguntaN9 = input('\033[;1m''''(9) Qual o significado das setas do símbolo internacional da reciclagem?\n
a) Fabricação, utilização e reutilização
b) Papel, vidro e metal
c) Papel, vidro e plástico
d) Lixo, reaproveitamento e fabricação
e) Coleta, separação e consumo
                        ''')
    resposta = pergunta9(perguntaN9) 
   
    perguntaN10 = input('\033[;1m''''(10) Qual dessas aves não voa?\n
a) Pinguim
b) Galinha
c) Cegonha
d) Pato
e) Peru
                        ''')
    resposta = pergunta10(perguntaN10) 
    break

print('\033[1;32m'f'Você acertou {quiz[1]} pergunta(s) e errou {quiz[2]}. ')
print('Fim.')
    


                                                            



    




    
    




    

       




