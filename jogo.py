import random
jogador1="luís"
jogador2="shadow"

opcoes=["pedra","papel","tesoura"]
decisao1=random.choice(opcoes)
decisao2=random.choice(opcoes)
print(f"{jogador1} usa {decisao1}")
print(f"{jogador2} usa {decisao2}")

while decisao1==opcoes[0]:
    if decisao2==opcoes[2]:
        print(f"{jogador1} ganhou")
    elif decisao2==opcoes[0]:
        print("empate")
    else:
        print(f"{jogador2} ganhou")
    break
while decisao1==opcoes[1]:
    if decisao2==opcoes[2]:
        print(f"{jogador2} ganhou")
    elif decisao2==opcoes[1]:
        print("empate")
    else:
        print(f"{jogador1} ganhou")
    break
while decisao1==opcoes[2]:
    if decisao2==opcoes[1]:
        print(f"{jogador1} ganhou")
    elif decisao2==opcoes[2]:
        print("empate")
    else:
        print(f"{jogador2} ganhou")
    break


