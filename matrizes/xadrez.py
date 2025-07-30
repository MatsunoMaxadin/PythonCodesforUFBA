matriz = []
hasEnemy = 0

for _ in range(8):
    linha = list(map(int,input().split()))
    matriz.append(linha)

X,Y = map(int,input().split())

for i in range(Y+1, 8, 1):
    if matriz[X][i] !=0:
        if matriz[X][i] == 2:
            hasEnemy += 1
        break  

for i in range(Y-1, -1, -1):
    if matriz[X][i]!=0:
        if matriz[X][i] == 2:
            hasEnemy += 1
        break 

for i in range(X+1, 8, 1):
    if matriz[i][Y] !=0:
        if matriz[i][Y] == 2:
            hasEnemy += 1
        break  

for i in range(Y-1, -1, -1):
    if matriz[i][Y]!=0:
        if matriz[i][Y] == 2:
            hasEnemy += 1
        break 


print(hasEnemy)
