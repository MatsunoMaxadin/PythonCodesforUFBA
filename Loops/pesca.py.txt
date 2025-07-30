N, T = map(int,input().split())
H = 0
pexe = 0

for i in range(N):
    H += int(input())

    if T >= H:
        pexe +=1

print(pexe)
