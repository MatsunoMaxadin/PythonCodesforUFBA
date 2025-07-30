numberOfSpheres = int(input())
balls = list(map(int,input().split()))
foundedBalls = []

for ball in balls:
    if 1 <= ball <= 7 and ball not in foundedBalls:
        foundedBalls.append(ball)

foundedBalls.sort()

print(' '.join(map(str, foundedBalls)))

if len(foundedBalls) == 7: 
    print("Saia Shenlong e realize o meu desejo")
else:
    print("Nao encontramos todas")
