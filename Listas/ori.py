M = int (input())
N = int(input())
X = list(map(int,input().split()))
B = list(map(int,input().split()))

T = 0

for i in range(N):
     T += X[i]*B[i]

if T >= M:
     print("Upou de Nivel!")
else:
    print("Nao foi dessa vez!")
