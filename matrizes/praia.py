ilha = []

for _ in range(10):
    linha = list(input().split())
    ilha.append(linha)


for i in range(10):
    for j in range(10):
        if ilha[i][j] == "t":
            if (i > 0 and ilha[i-1][j]=="*") or (i < 9 and ilha[i+1][j]=="*") or (j > 0 and ilha[i][j-1]=="*") or (j < 9 and ilha[i][j+1]=="*"):
                ilha[i][j] = "p"

for l in range(10):
    for c in range(10):
        print(ilha[l][c], end=" ")
    print()
