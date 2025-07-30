N = int(input())
hasJelly = 0
noJelly = 0    

for i in range(N):
      order = int(input())
      
      if order == 10:
          noJelly +=1
      else:
          hasJelly+=1


if hasJelly >= noJelly:
   print("Geleia")
else:
   print("Tradicional")
