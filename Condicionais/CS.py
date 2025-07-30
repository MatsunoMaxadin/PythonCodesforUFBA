L1, P1 = map(int, input().split())
L2, P2 = map(int, input().split())
L3, P3 = map(int, input().split())

L = L1+L2+L3
P = P1+P2+P3

if L > P:
    print('Lucas')
elif P > L:
    print('Pedro')
else:
    print('Empate')
