z,g = input().split()
d,c = input().split()

isDribbled = z == d 
isGoal = g == c

if not isDribbled:
    print('Bloqueado')
elif isDribbled and not isGoal:
    print('Driblado')
    print('...e o goleiro pega')
else:
    print('Driblado')
    print('Gol')
