n1, n2, n3, n4 = input().split()

n1 = float(n1)*2

n2 = float(n2)*3

n3 = float(n3)*4

n4 = float(n4)


media = ((n1+n2+n3+n4)/10)

print('Media: %.1f' %media)


if (media>=7.0):

  print('Aluno aprovado.')

elif (media<5.0):

  print('Aluno reprovado.')
#VERIFICAR LINHA ABAIXO
elif ((media>=5.0) and (media<=6.9)):

  print('Aluno em exame.')

  n5 = float(input())

  final = (n5+media)/2

  print('Nota do exame:', n5)

  if (final>=5.0):

    print('Aluno aprovado.')

    print('Media final: %.1f' %final)

  elif (final<=4.9):
# VERIFICAR LINHA ABAIXO
    print('Aluno reprovado')

    print('Media final: %.1f' % final)




# 2.0 - 4.0 - 7.5 - 8.0 - 2.2
