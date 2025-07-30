n = int(input())
fases = list(map(int,input().split()))
vida_max = int(input())

vida = vida_max
morreu = False

for fase in fases:
    if fase == 0:
        continue
    elif fase == 1:
        vida = vida_max
    else: 
        vida -= fase
    
    if vida <= 0:
        morreu = True
        break


if morreu:
    print("You Died")

else:
    print("Yes, you can")
