import random 

def jogo_advinhação():
    numero_secreto = random.randint(1,100)
    tentativas = 0


print("Bem-vindo ao jogo da advinhação!")
print("Estou pensando em um número entre 1 e 100")


while True:
    try:
        palpite = int(input("Digite seu palpite"))
        tentativas += 1

        if palpite < numero_secreto:
            print("Um pouco maior")

        elif palpite > numero_secreto:
            print("Um pouco maior")

        else:
             print("Parabens você acertou o número em {tentativas }tentativas")
             break
        
    except ValueError:
        print("Por favor, adicione um número válido")

if __name__ == "__main__":
    Jog0_advinhação()