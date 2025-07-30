sections = int(input())
comprimentos = list(map(int,input().split()))
totalSum = 0
thisSum = 0
p = 0

for section in comprimentos:
    totalSum += section 

mediana = totalSum//2 

for i in range(sections):
    thisSum += comprimentos[i]
    if thisSum >= mediana:
        p = i+1
        break

print(p)
    
