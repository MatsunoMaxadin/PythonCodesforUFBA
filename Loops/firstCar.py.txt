N, Y = input().split()

N = int(N)
Y = float(Y)
X = 0
M = 0

for i in range(1, (N+1)):
      X += float(input())

      if X >= Y and M==0: 
         M = i
         X -= Y

