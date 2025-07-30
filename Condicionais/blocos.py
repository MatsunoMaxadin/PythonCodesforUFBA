C,c,x = map(int, input().split())

width = C/c

total = width**3 

if total > x:
    print('!Eh possivel')
else: 
    print('Eh possivel')
