F,C = map(int,input().split())
cinema = []
for i in range(F):
    lista = list(map(int,input().split()))
    cinema.append(lista)

Fileira = 0
Assentox = 0
Assentoy = 0
for i in range(F):
    for j in range(C):
        if cinema[i][j] == 0 and j < C-1:
            if cinema[i][j+1] == 0:
                Fileira = i+1
                Assentox = j+1
                Assentoy = j+2
                break 
    
                
print(f'Fileira: {Fileira}')
print(f'Assentos: {Assentox} e {Assentoy}')
