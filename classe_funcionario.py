import os
os.system

# Criando classe funcionario e seus atributos
class Funcionario:
    def __init__(self, nome, salario, gerente):
        self.__nome = nome
        self.__salario = salario
        self.__gerente = gerente

    def nome(self):
        return self.__nome

    def salario(self):
        return self.__salario

    def gerente(self):
        return self.__gerente
