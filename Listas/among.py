players = int(input())

kills = list(map(int,input().split()))

indices = [0]*(max(kills)+1)

orderedKills = []

for i in kills:
    indices[i] = 1

for i in range (len(indices)):
    if indices[i] == 1:
        orderedKills.append(i)

print(' '.join(map(str, orderedKills)))
    
