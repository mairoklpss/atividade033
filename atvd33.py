#faças as modifições pedintes na lista.

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print('a lista é:', num)
print('intavelo de 1 a 9:', num[1:10])
print('intervalo de 8 a 13:', num[8:14])
print('números pares:', num[::2])
print('números ímpares:', num[1::2])
print('múltiplos de 2:', num[2::2])
print('múltiplos de 3:', num[3::3])
print('múltiplos de 4:', num[4::4])

#lista reversa
num.reverse()
print('lista reversa:', num)

#voltar ao normal
num.sort()

print('razão:', sum(num[10:16]), '/', sum(num[3:9]), "ou", sum(num[10:16])/sum(num[3:9]))

