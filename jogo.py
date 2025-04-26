"""Você está criando um programa em Python para simular
 um jogo simples de adivinhação. O programa deve ter um 
 número fixo, por exemplo, 7, que o jogador deve adivinhar.
   O jogador terá até 3 tentativas para acertar o número.
Implemente o jogo utilizando um loop while para permitir que
 o jogador faça múltiplas tentativas até acertar ou atingir o 
 limite de tentativas. Utilize a estrutura else para exibir uma
   mensagem de encorajamento caso o jogador acerte e uma mensagem
     de consolo caso as 3 tentativas se esgotem sem sucesso."""

# Número fixo a ser adivinhado

# O número que o usuário deve adivinhar é 7 (fixo no código).
numero_secreto = 7
tentativas_restantes = 3  # O usuário tem 3 tentativas para acertar.

# Exibe a mensagem inicial
# Apresenta as regras do jogo e informa o número de tentativas disponíveis.

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto (entre 1 e 10). Você tem 3 tentativas.")

# Cria o loop while para gerenciar as tentativas
# O loop continua rodando enquanto o usuário ainda tiver tentativas.
# O usuário tem no máximo 3 tentativas antes de o jogo terminar.

while tentativas_restantes > 0:
    # Solicita o palpite do usuário , Converte a resposta para um número inteiro (int).
    palpite = int(input("Digite seu palpite: "))
    # Reduz o número de tentativas / Toda vez que o usuário faz um palpite, uma tentativa é descontada.
    tentativas_restantes -= 1

# Verifica se o palpite está correto
# Se o palpite for igual ao número secreto (7), o jogo termina imediatamente e o usuário vence.

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break  # O break interrompe o loop, impedindo novas tentativas.
    else:  # Se o palpite estiver errado, informa quantas tentativas restam
        # Se o palpite for errado:/ Se ainda restarem tentativas, o jogo informa quantas tentativas sobraram.
        if tentativas_restantes > 0:
            print(
                f"Errado! Você tem {tentativas_restantes} tentativas restantes.")
        else:  # Se acabarem as tentativas, exibe a mensagem final
            # Se o usuário errar todas as tentativas, aparece a mensagem de que as tentativas acabaram.
            print("Suas tentativas acabaram.")

else:  # Mensagem final do jogo
    print("Que pena! Você não conseguiu adivinhar o número secreto desta vez. Boa sorte na próxima!")
