# Usando laço de repetição WHILE

# Cadastro
class SistemUser():

    def __init__(self):
        username = ''
        password = 'default_pass'
        pass_validation = 'default_validation_pass'
        self.username = username
        self.password = password
        self.pass_validation = pass_validation
        print('Classe recebida, instância criada')

    def sign_up(self):
        while len(self.username) < 8:
            self.username = input(f"Bem Vindo!\n\nCrie um nome de usuário\n{'-' * 50}\n-> Um nome de usuário válido deve conter no mínimo 8 caracteres: ")

        while self.password != self.pass_validation:
            self.password = input(f'Crie uma senha válida e segura: ')
            self.pass_validation = input(f'Agora confirme sua senha, deve ser igual a senha digitada anteriormente: ')
    
    def log_in(self):
        typed_username = ''
        typed_password = ''

        while self.username != typed_username:
            typed_username = input(f'Seu Usuário: ')
        
        while self.password != typed_password:
            typed_password = input(f'Sua Senha: ')

j = SistemUser()
j.sign_up()
j.log_in()