numberOfObstacles = int(input())
obstacleHeight = list(map(int,input().split()))
maxJumpHeight = int(input())
jumpedObstacles = 0
hasJumpedAll = 1

for i in range(numberOfObstacles):
    if maxJumpHeight >= obstacleHeight[i]:
        jumpedObstacles += 1
    else:
        hasJumpedAll = 0
        break



print(jumpedObstacles)
print(hasJumpedAll)
