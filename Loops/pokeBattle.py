enemyHP, power = map(int,input().split())
i = 0

while enemyHP > 0:

    enemyHP -= power
    power -= 1
    i+=1

    if power == 0 and enemyHP > 0:
        print("F")
        break

if enemyHP <= 0:
    print(i)
