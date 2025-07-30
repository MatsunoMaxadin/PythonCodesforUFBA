N, M = map(int, input().split())
matriz = []
isDestroyed = 0

# Leitura da matriz
for _ in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Processamento dos teleportes
for _ in range(M):
    L, C = map(int, input().split())

    # Validação dos limites corretos (0 ≤ L < N, 0 ≤ C < N)
    if 0 <= L < N and 0 <= C < N:
        # Luke atira para cima, verifica de (L-1) até 0
        for i in range(L - 1, -1, -1):
            if matriz[i][C] == 1:
                isDestroyed += 1
                matriz[i][C] = 0  # nave destruída
                break  # só a primeira nave é destruída

print(isDestroyed)
