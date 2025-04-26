#votação
def main():
#declaração de variáveis constantes
    vote_ana = 0
    vote_rodrigo = 0
    vote_edson = 0
    vote_karina = 0
#inicio de laço do repetição
    while True:
        print("Bem-vindo à urna eletrônica!")
        print("Escolha seu candidato:")
        print("1. Ana")
        print("2. Rodrigo")
        print("3. Edson")
        print("4. Karina")

        escolha = input("Precione o número do seu candidato: ")
        if escolha == '1':
            vote_ana += 1
        elif escolha == '2':
            vote_rodrigo += 1
        elif escolha == '3':
            vote_edson += 1
        elif escolha == '4':
            vote_karina += 1
        elif escolha == '5':
            senha = input("Digite a senha para prosseguir")
            if senha == "SejaCrocanteNoLeite":
                print("Exibindo resultados:")
                print("Ana", vote_ana) 
                print("Breno", vote_rodrigo)
                print("Carla", vote_edson)
                print("Danilo", vote_karina)  
            else: 
                print("Acesso negado!")
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

        print("Obrigado por votar!")

if __name__ == "__main__":
    main()


