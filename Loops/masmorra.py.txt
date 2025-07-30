N = int(input())
L = 0

level = 1
monsterLevel = 0

for i in range(N):
    door, number = input().split()


    if door == "t":
        level += int(number)
    elif door == "m":
        print("Combate iniciado")
        monsterLevel = int(number)
        if level >= monsterLevel:
            level += 1
            print("VITORIA")
        else:
            print("Derrota! Fim da aventura")
            break
    elif door == "b":
        level -= int(number)

        if level < 0:
            level = 0
    
    if level == 5:
        print("Aventura concluida")
        break 
