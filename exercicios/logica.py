#5. Simule login — o usuário tem 3 tentativas pra digitar a senha "dev2024". Se errar as 3, mostra "Conta bloqueada".
senha_correta = "dev2024"
senha = input("Digite sua senha: ")
tentativas = 3

while senha != senha_correta and tentativas > 0:
    tentativas -= 1
    print(f"Senha incorreta.\n {tentativas} tentativas restantes.")
    senha = input("Digite sua senha: ")

if tentativas == 0:
    print("Conta bloqueada.")
elif senha == senha_correta:
    print("Bem-vindo!")