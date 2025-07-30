M,N = map(int,input().split())
matriz = []
c = 0
Sum = 0




for i in range(M):
    linha = list(map(int,input().split()))
    matriz.append(linha)

T,P = input().split()
P = int(P)
    
for linha in matriz:
    if T == "L" and c == P-1 and P-1 <= M:
        Sum = sum(linha)
        break
    elif T == "C" and P-1 <= N:
        Sum += linha[P-1]
    c+=1

print(Sum)
