N,M = map(int,input().split())
caminho = []
ovos = 0

for i in range(N):
    lista = list(map(int,input().split()))
    caminho.append(lista)


for i in range(N):
    if i%2 == 0:
        for j in range(M):
            if ovos + caminho[i][j] > 0 :
                ovos += caminho[i][j]
            else:
                ovos = 0
            caminho[i][j] = 0
    if i%2 == 1:
        for j in range(M-1, -1, -1):
            if ovos + caminho[i][j] > 0 :
                ovos += caminho[i][j]
            else:
                ovos = 0
            caminho[i][j] = 0
 


print (ovos)
