# Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.
senha = str(input('Informe a senha:\n'))
while senha == '1234':
    print("Senha válida!")
    break


