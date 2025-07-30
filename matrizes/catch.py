N, M = map(int, input().split())

matriz = []

for _ in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)

P = int(input())


Q = 0
for linha in matriz:
    Q += linha.count(P)

print(f'Ash pegou {Q} pokemon')
