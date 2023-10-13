def converte(temp):
    c = 5* ((temp-32)/9)

    return c

temp = float(input('TEMPERATURA EM Fahrenheit: '))

print('CELSIUS: {:.1f}'.format(converte(temp)))
