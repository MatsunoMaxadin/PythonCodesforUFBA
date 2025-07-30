x,y = map(int, input().split())

isValid = x > 0 and y > 0 and x < 100 and y < 100

isFar = x > 70 or y > 70


if not isValid:
    print('Coordenada invalida')
elif isValid and isFar:
    print('Coordenada valida e o navio esta longe')
else:
    print('Coordenada valida e o navio esta perto')
