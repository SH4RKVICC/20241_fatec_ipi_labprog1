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
    
# Aplicando aumento para 5% para funcionario e 8% se o funcionario for gerente
    def aplicar_aumento(self):
        if self.__gerente:
            aumento = 0.08
        else:
            aumento = 0.05
        print(f"Aumento em {aumento}% aplicado com sucesso.")
        novo_sal = self.__salario * (aumento)
        self.__salario += novo_sal