#criando classe tamaguchi com nome, fome, saude e idade
class Tamaguchi:
    def __init__ (self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

#o humor depende se a fome e a saude estão em estado positivo (true)
def humor(self):
    if self.fome and self.saude:
        print("Seu tamaguchi está de bom humor!")
    else:
        print("Seu tamaguchi está de mal humor!")

#Teste Tamaguchi
t = tamaguchi("Adam Driver", False, True, 9)
t.humor()