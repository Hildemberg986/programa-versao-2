def clear():
    import os
    import platform
    desk = platform.system()
    if desk == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def menu():
    clear()
    print('==================================')
    print('========  MENU PRINCIPAL  ========')
    print('==================================')
    print('   1 - CADASTRAR CLIENTE')
    print('   2 - PESQUISAR CLIENTE')
    print('   3 - MODIFICAR CLIENTE')
    print('   4 - DELETAR CLIENTE')
    print('   0 - SAIR')
    option = input('Escolha sua opção ? ')
    return option
op = menu()
while op != '0':
  if op == '1':
    clear()
    print ('opção 1')
  elif op == '2':
    clear()
    print ('opção 2')
  elif op == '3':
    clear()
    print('opçao 3')
  elif op == '4':
    clear()
    print ('opção 4')
  else:
    clear()
    print ('Opção invalida!')
  input("Precione enter para continuar...")
  op = menu()
clear()
print ('Programa encerrado!')
