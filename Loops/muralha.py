notion = ' '
finalMessage = 'Muralha congelantemente tranquila'
CB = 0

while notion != 'FIM':
    notion = input()

    if notion == 'Caminhante Branco':
        CB += 1
        if CB == 1:
            print('Soar alarme e ficar alerta')

if CB == 0:
    print(finalMessage)
print(f'Caminhante Branco: {CB}')
