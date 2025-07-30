x, y =  map(int, input().split())

d = y*9

if d>=x:

  print('Lar doce lar.')

elif (x-d)%9 != 0:
       print('Precisa de mais difusores!')
       print((x-d)// 9 + 1)
else:
      print('Precisa de mais difusores!')
      print((x-d)// 9)
