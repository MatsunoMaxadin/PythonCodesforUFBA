I,N,P = map(int,input().split())

isAgeValid = I > 17
doHaveLicence = N > 0
HasMinScore = P >= 80

if doHaveLicence:
    HasMinScore = P >=60


if isAgeValid and HasMinScore:
    print('Candidato apto para o exame pratico. Boa sorte!')
else:
    print('Candidato nao atende aos requisitos. Tente no proximo ano.')
