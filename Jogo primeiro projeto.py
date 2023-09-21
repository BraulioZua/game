# Jogo de pedra, papel, ou tesoura

#0.1 Instanciar uma variavel- 
import random
user= input ("escolhe uma opçao")
pc= random.choice(("pedra", "papel", "tesoura"))

#0.2 Logica
if user == "papel" and pc == "papel":
	Resultado= ("o user Empatou")

if user  == "tesoura" and pc == "papel":
	Resultado= ("o user Venceu")

if user  == "pedra" and pc == "papel":
	Resultado= ("O user Perdeu")


if user  == "papel" and pc == "tesoura":
	Resultado= ("O user Perdeu")


if user  == "tesoura" and pc == "tesoura":
	Resultado= ("o user Empatou")


if user  == "pedra" and pc == "tesoura":
	Resultado= ("o user Venceu")


if user  == "papel" and pc == "pedra":
	Resultado= ("o user Venceu")


if user  == "tesoura" and pc == "pedra":
	Resultado= ("O user Perdeu")


if user  == "pedra" and pc == "pedra":
	Resultado= ("o user Empatou")


#0.3 resultado

print(Resultado)
print("user", user, "pc", pc)
