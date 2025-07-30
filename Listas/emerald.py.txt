number = int(input())
N = list(map(int, input().split()))
C = int(input())
Emerald = -1

for i in range(len(N)):
    if N[i]==C:
        Emerald = C
        break
print (Emerald)
