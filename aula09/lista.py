from audioop import reverse


cavaleiros = ["Seya", "Shun", "Shiryu", "Yoga"]
print(cavaleiros)

# adicona um novo elemento ao final da lista:
cavaleiros.append("Ikki")
print(cavaleiros)
print('-='*60)

# adiciona à lista com outra lista
cavaleiros.extend(['Shina','Maryn'])
print(cavaleiros)
print('-='*60)

# inserir na lista em uma posição específica
cavaleiros.insert(0, "Athena")
print(cavaleiros)
print('-='*60)

# remove - exclui um elemento pelo valor do elemento
cavaleiros.remove('Shun')
print(cavaleiros)
print('-='*60)

# pop - exclui o último elemento da lista ou o índice informado
cavaleiros.pop()
print(cavaleiros)
elemento = cavaleiros.pop()
print(elemento)
cavaleiros.pop(0)
print(cavaleiros)
print('-='*60)

# index - retorna o índice da primeira ocorrência de um valor procurado
print(cavaleiros.index("Yoga"))
cavaleiros.pop(cavaleiros.index("Yoga"))
print(cavaleiros)
# Alterando o valor de um elemento da lista
cavaleiros[cavaleiros.index("Ikki")] = "Ikki de Fênix"
print(cavaleiros)
print('-='*60)

# Contabilizando
cavaleiros2 = ["Seya", "Aldebaran", "Aldebaran", "Shun", "Shiryu", "Yoga"]
print(cavaleiros2)
print(cavaleiros2.count("Aldebaran"))
print('-=')

# sort - organiza a lista em orde, crescente ** default **
frutas = ['morango', 'maçã', 'abacaxi', 'amora', 'umbu', 'kiwi', 'laranja', 'bergamota']
numeros = [9, 5, 81, 100, 33, 21, 2]
frutas.sort()
numeros.sort()
print(frutas)
print(numeros)
print('-='*60)

# reverse - organiza a lista em ordem decrescente
frutas.reverse()
numeros.reverse()
print(frutas)
print(numeros)
print('-='*60)

# apaga o elemento pelo índice, ou, caso o índice não seja informado, apaga a lista toda
del frutas[0]
print(frutas)
print('-=')

# limpar a lista
frutas.clear()
print(frutas)
print('-=')

# apaga a lista toda
del frutas
print(frutas) # a lsiat não pode ser impressa porque não existe mais

