print('Valor nutricional Habbis')
from time import sleep
calabresa = [8.4, 115, 4.8, 6.9, 339]
espinafre = [19, 158, 4, 7.1, 267]
carne = [20, 171, 5.4, 7.9, 346]
frango = [19, 152, 6.4, 5.6, 313]
italiana = [8.5, 128, 7.5, 7.2, 195]
queijo = [18, 184, 9.7, 7.9, 162]
fourqueijo = [8.3, 177, 8.5, 12, 277]
frangocream = [21, 166, 8.4, 5.3, 341]

'''carboidrato 
    calorias 
    proteinas
    gordura
    sodio'''

esfirra01 = int(input('Quantas  BIB’SFIHA DE CALABRESA COM MUSSARELA VOCÊ COMEU OU VAI COMER?'))
esfirra02 = int(input('Quantas  BIB´SFIHA DE ESPINAFRE E PHILADELPHIA VOCÊ COMEU OU VAI COMER?'))
esfirra03 = int(input('Quantas  BIB´SFIHA DE CARNE VOCÊ COMEU OU VAI COMER?'))
esfirra04 = int(input('Quantas  BIB´SFIHA DE FRANGO VOCÊ COMEU OU VAI COMER?'))
esfirra05 = int(input('Quantas  BIB’SFIHA ITALIANINHA VOCÊ COMEU OU VAI COMER?'))
esfirra06 = int(input('Quantas  BIB’SFIHA DE QUEIJO VOCÊ COMEU OU VAI COMER?'))
esfirra07 = int(input('Quantas  BIB’SFIHA 4 QUEIJOS VOCÊ COMEU OU VAI COMER?'))
esfirra08 = int(input('Quantas  BIB’SFIHA DE FRANGO COM CREMELY VOCÊ COMEU OU VAI COMER?'))

if esfirra01 != 0:
    print(f'\033[1:40m Esfirra de calabresa com mussarela Quantidades[{esfirra01}]: \n Calorias: {calabresa[1] * esfirra01:_.2f}kcal \n Carboidratos: {calabresa[0] * esfirra01:_.2f}g \n'
          f' proteínas: {calabresa[2] * esfirra01:_.2f}g \n Gordura: {calabresa[3] * esfirra01:_.2f}g \n Sódio: {calabresa[4] * esfirra01:}mg')
sleep(1)

if esfirra02 != 0:
    print(f'\033[0:1:40mEsfirra de espinafre Quantidades[{esfirra02}]: \n Calorias: {espinafre[1] * esfirra02}kcal \n Carboidratos: {espinafre[0] * esfirra02}g \n'
        f' proteínas: {espinafre[2] * esfirra02:_.2f}g \n Gordura: {espinafre[3] * esfirra02:_.2f}g \n Sódio: {espinafre[4] * esfirra02}mg')
sleep(1)

if esfirra03 != 0:
    print(f'\033[0:1:40mEsfirra de carne Quantidades[{esfirra03}]: \n Calorias: {carne[1] * esfirra03}kcal \n Carboidratos: {carne[0] * esfirra03}g \n'
        f' proteínas: {carne[2] * esfirra03:_.2f}g \n Gordura: {carne[3] * esfirra03:_.2f}g \n Sódio: {carne[4] * esfirra03}mg')
sleep(1)

if esfirra04 != 0:
    print(f'\033[0:1:40mEsfirra de frango Quantidades[{esfirra04}]: \n Calorias: {frango[1] * esfirra04}kcal \n Carboidratos: {frango[0] * esfirra04}g \n'
        f' proteínas: {frango[2] * esfirra04:_.2f}g \n Gordura: {frango[3] * esfirra04:_.2f}g \n Sódio: {frango[4] * esfirra04}mg')
sleep(1)

if esfirra05 != 0:
    print(f'\033[0:1:40mEsfirra Italiana Quantidades[{esfirra05}]: \n Calorias: {italiana[1] * esfirra05}kcal \n Carboidratos: {italiana[0] * esfirra05}g \n'
        f' proteínas: {italiana[2] * esfirra05:_.2f}g \n Gordura: {italiana[3] * esfirra05:_.2f}g \n Sódio: {italiana[4] * esfirra05}mg')
sleep(1)

if esfirra06 != 0:
    print(f'\033[0:1:40mEsfirra de queijo Quantidades[{esfirra06}]: \n Calorias: {queijo[1] * esfirra06}kcal \n Carboidratos: {queijo[0] * esfirra06}g \n'
        f' proteínas: {queijo[2] * esfirra06:_.2f}g \n Gordura: {queijo[3] * esfirra06:_.2f}g \n Sódio: {queijo[4] * esfirra06}mg')
sleep(1)

if esfirra07 != 0:
    print(f'\033[0:1:40mEsfirra de 4 queijos  Quantidades[{esfirra07}]: \n Calorias: {fourqueijo[1] * esfirra07}kcal \n Carboidratos: {fourqueijo[0] * esfirra07:_.2f}g \n'
        f' proteínas: {fourqueijo[2] * esfirra07:_.2f}g \n Gordura: {fourqueijo[3] * esfirra07:_.2f}g \n Sódio: {fourqueijo[4] * esfirra07}mg')
sleep(1)

if esfirra08 != 0:
    print(f'\033[0:1:40mEsfirra de frango com cremely Quantidades[{esfirra08}]: \n Calorias: {frangocream[1] * esfirra08}kcal \n Carboidratos: {frangocream[0] * esfirra08}g \n'
        f' proteínas: {frangocream[2] * esfirra08:_.2f}g \n Gordura: {frangocream[3] * esfirra08:_.2f}g \n Sódio: {frangocream[4] * esfirra08}mg')


sleep(1)
print(f'\033[1:34mTotal de esfirras: {esfirra01 + esfirra02 + esfirra03 + esfirra04 + esfirra05 + esfirra06 + esfirra07 + esfirra08}')
if esfirra01 != 0:
    print(f'Esfirra de calabresa com mussarela: {esfirra01}')
if esfirra02 != 0:
    print(f'Esfirra de espinafre: {esfirra02}')
if esfirra03 != 0:
    print(f'Esfirra de carne: {esfirra03}')
sleep(1)
if esfirra04 !=0:
    print(f'Esfirra de frango: {esfirra04}')
if esfirra05 !=0:
    print(f'Esfirra Italiana:{esfirra05}')
if esfirra06 != 0:
    print(f'Esfirra de queijo: {esfirra06}')
if esfirra07 !=0:
    print(f'Esfirra quatro queijos: {esfirra07}')
if esfirra08 != 0:
    print(f'Esfirra de frango com cremely: {esfirra08}')

sleep(1)
print(f'\033[1:33mTotal de calorias:{calabresa[1] * esfirra01 + espinafre[1] * esfirra02 + carne[1] * esfirra03 + frango[1] * esfirra04 + italiana[1] * esfirra05 + queijo[1] * esfirra06 + fourqueijo[1] * esfirra07 + frangocream[1] * esfirra08} calorias')
print(f'Total de carboidratos:{calabresa[0] * esfirra01 + espinafre[0] * esfirra02 + carne[0] * esfirra03 + frango[0] * esfirra04 + italiana[0] * esfirra05 + queijo[0] * esfirra06 + fourqueijo[0] * esfirra07 + frangocream[0] * esfirra08:_.2f} gramas')
print(f'Total de proteínas:{calabresa[2] * esfirra01 + espinafre[2] * esfirra02 + carne[2] * esfirra03 + frango[2] * esfirra04 + italiana[2] * esfirra05 + queijo[2] * esfirra06 + fourqueijo[2] * esfirra07 + frangocream[2] * esfirra08:_.2f} gramas')
print(f'Total de gordura:{calabresa[3] * esfirra01 + espinafre[3] * esfirra02 + carne[3] * esfirra03 + frango[3] * esfirra04 + italiana[3] * esfirra05 + queijo[3] * esfirra06 + fourqueijo[3] * esfirra07 + frangocream[3] * esfirra08:_.2f} gramas')
print(f'Total de Sódio:{calabresa[4] * esfirra01 + espinafre[4] * esfirra02 + carne[4] * esfirra03 + frango[4] * esfirra04 + italiana[4] * esfirra05 + queijo[4] * esfirra06 + fourqueijo[4] * esfirra07 + frangocream[4] * esfirra08} mg')