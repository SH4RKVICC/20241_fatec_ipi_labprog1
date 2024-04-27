
#criando classe aluno com atributo nome
class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Aluno: {self.nome}"

#criando classe professor com atributo nome e titulação
class Professor:
    def __init__(self, nome, titulacao):
        self.nome = nome
        self.titulacao = titulacao

    def __str__(self):
        return f"Professor: {self.nome}, Titulação: {self.titulacao}"