import random

def jogar():
    imprimir_abertura()
    continuar = 's'

    while (continuar != "n"):
        palavra_secreta = escolher_palavra()
        letras_acertadas = cria_letras_acertadas(palavra_secreta)
        letras_erradas = []
        
        forca = False
        acertou = False
        erros = 0

        print(" ".join(letras_acertadas))

        while ((not forca) and (not acertou)):
            
            chute = perguntar_chute()
            
            if (len(chute) == 1): 
                if(chute in palavra_secreta):
                    substituir_tracinhos(palavra_secreta, chute, letras_acertadas)
                else:
                    if (chute not in letras_erradas):
                        letras_erradas.append(chute)
                    erros += 1
            elif (len(chute) > 1):
                if (chute == 'SAIR'):
                    exit()
                elif (chute == 'CHEAT1'):
                    letras_erradas.append(chute)
                elif  (chute == 'CHEAT0'):
                    erros = cheat_code0(chute, erros)
                elif(chute == palavra_secreta):
                    letras_acertadas = palavra_secreta
                else:
                    if (chute not in letras_erradas):
                        letras_erradas.append(chute)
                    erros += 1
            
            forca = erros == 6
            acertou = "_" not in letras_acertadas

            imprimir_forca(erros)
            print(" ".join(letras_acertadas))

            cheat_code1(chute, palavra_secreta, letras_erradas)

            erradas = ",  ".join(letras_erradas)
            print(f"Erros: {erros}{' '*3}Letras Erradas: {erradas}")
        imprime_mensagem_endgame(acertou, palavra_secreta)

        continuar = input(f"Quer continuar jogando? [s] ou [n] ")
   
def imprimir_abertura():
    print(f"\n{'*'*33}\n{'*'*2} Bem vindo ao jogo de Forca! {'*'*2}\n{'*'*33}")

def escolher_palavra():
    with open("palavras.txt", "r") as arquivo_de_palavras:
        palavras = [linha.strip().upper() for linha in arquivo_de_palavras]

    random.shuffle(palavras)

    palavra_secreta = palavras[random.randrange(0,len(palavras))]
    return palavra_secreta

def cria_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def perguntar_chute():
    return (input('Qual a letra?: ')).strip().upper()

def substituir_tracinhos(palavra, chute,letras):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras[index] = letra
        index += 1

def cheat_code0(code, erros):
    if (code == "CHEAT0"):
        return 0
    else:
        return erros

def imprimir_forca(erros):
    print('____')
    if (erros == 0):
        print('|/')
        print('|')
        print('|')
        print('|')
        print('|___')
    elif (erros == 1):
        print('|/ O')
        print('|')
        print('|')
        print('|')
        print('|___')
    elif (erros == 2):
        print('|/ O')
        print('| /')
        print('|')
        print('|')
        print('|___')
    elif (erros == 3):
        print('|/ O')
        print('|  Ʌ')
        print('|')
        print('|')
        print('|___')
    elif (erros == 4):
        print('|/ O')
        print('|  Ʌ')
        print('|  |')
        print('|')
        print('|___')
    elif (erros == 5):
        print('|/ O')
        print('|  Ʌ')
        print('|  |')
        print('|  /')
        print('|___')
    elif (erros == 6):
        print('|/(x-x)')
        print('|   Ʌ')
        print('|   |')
        print('|   Ʌ')
        print('|___')

def cheat_code1(code, palavra_secreta, lista):
    if (code == 'CHEAT1'):
        print(f"cheat: {palavra_secreta}")
        lista.remove('CHEAT1')

def imprime_mensagem_endgame(acertou, palavra):
    if (acertou and (palavra == 'DADO^-^')):
        easter_egg()
    elif (acertou):
        print('!!! VOCÊ ACERTOU !!!')
    else:
        print(f"!!! VOCÊ FOI ENFORCADO !!!\nPalavra: {palavra}")
        
    print(f"Fim do jogo\n{'_'*75}\n")

def easter_egg():
    print(r"           _____    _____  _____    _____  ")
    print(r"  _____    |  _ \  /  _  \ |  _ \  /  _  \ ")
    print(r" / .  /\   | | \ \ | |_| | | | \ \ | | | | ")
    print(r"/____/..\  | | | | |  _  | | | | | | | | | ")
    print(r"\'  '\  /  | |_/ / | | | | | |_/ / | |_| | ")
    print(r" \'__'\/   |____/  |_| |_| |____/  \_____/ ")
    

if(__name__ == "__main__"):
    jogar()
 

          