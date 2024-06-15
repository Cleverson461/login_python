#Defina um usuario e senha e depois verifique se login do usuario é valido.

usuario = 'Cleverson'
senha = '1234'

while True:
    usuario_login = input('Digite o usuário: ')
    senha_login = input('Digite a senha: ')

    if usuario_login == usuario and senha_login == senha:
      print('Usuário e senha válidos.')
      break
    else:
        print('Usuário e senha inválidos.')
#print(f'Usuário e senha válidos com sucesso. {usuario} e {senha}.')