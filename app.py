"""Crie um programa em Python que simule um sistema de login.
 O programa deve permitir ao usuário três tentativas para acertar
   o nome de usuário e a senha corretos. Caso o usuário erre as 
   credenciais, o programa deve fornecer uma mensagem informando 
   quantas tentativas restam. Se o usuário acertar, uma mensagem 
   de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.



Se todas as três tentativas falharem, o programa deve usar um loop for para
 exibir uma mensagem de "Acesso bloqueado" repetida três vezes."""


# # Define o nome de usuário  e a senha  corretos.
# usuario, senha = "admin", "1234"
# # Cria um loop que vai rodar 3 vezes, ou seja, 3 tentativas.
# for i in range(3):
#     # Pede o usuário e a senha. Se os dois estiverem corretos, imprime "Bem-vindo!" e break encerra o loop imediatamente.
#     if input("Usuário: ") == usuario and input("Senha: ") == senha:
#         print("Bem-vindo!")
#         break
#     # Se errou, mostra quantas tentativas ainda restam (2, 1 ou 0). O i começa em 0, então 2 - i dá exatamente o número de tentativas restantes.
#     print(f"Tentativas restantes: {2 - i}")
# else:  # Esse else pertence ao for, e só executa se o loop terminar sem o break, ou seja, se o usuário errou as 3 tentativas.
#     for i in range(3):
#         # Nesse caso, um novo for mostra "Acesso bloqueado." 3 vezes.
#         print("Acesso bloqueado.")

# # EM CASO DE USUARIO E SENHA CORRETOS
# usuario, senha = "admin", "1234"
# for i in range(3):
#     if input("Usuário: ") == usuario and input("Senha: ") == senha:
#         print("Olá, seu acesso foi liberado!")
#         break

# # EM CASO DE USUARIO E SENHA ERRADOS

#     print(f"Tentativas restantes: {2 - i}")

# else:
#     for i in range(3):
#         print("Senha e usuario digitados não coferem, seu acesso foi bloqueado.")


# EM CASO DE ACERTO

# usuario, senha = "Veryfloe82@", "042510336448215"
# for i in range(3):
#     if input("Por favor digite o usuário: ") == usuario and input("Agora digite a sua senha: ") == senha:
#         print("Acesso liberado!")
#         break

#     # EM CASO DE ERRO DO USUARIO E SENHA
#     print(f"Usuário e senha incorretos,restam {2 - i} tentativas.")

# else:
#     for i in range(3):
#         print("Você excedeu o número de tentativas. ACESSO BLOQUEDO!!!  ")

usuario, senha = "Veryfloe82@", "042510336448215"

for i in range(3):
    if input("Por favor,digite o seu usuário: ") == usuario and input("Agora digite a sua senha: ") == senha:
        print("Usuário e senha corretos,ACESSO LIBERADO!!!")
        break

    print(f"Usuário e senha incorretos, restam {2 - i} tentativas.")

else:
    for i in range(3):
        print("Você excedeu o número de tentativas. ACESSO BLOQUEDO!!!")