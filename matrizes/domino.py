matriz = []

for i in range(7):
    linha = list(map(int,input().split()))
    matriz.append(linha)

hasPeace = 0

for i in range(7):
    for j in range(i+1):
        if matriz[i][j] == 1:
            hasPeace+= 1
    

print(hasPeace)
