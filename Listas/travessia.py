S, N = map(int, input().split())
jump = []

for i in range(S):
     jump.append(int(input()))


isJumped = [0]*N
isJumped[0] = 1

for i in range(S):
    for j in range(N):
        if j !=0:
            if j%jump[i] == 0:
                isJumped[j] = 1


for i in isJumped:
    print(i, end=" ")
