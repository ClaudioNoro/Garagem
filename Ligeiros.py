# Ligeiros.py
from Veiculo import Veiculo

class Ligeiros(Veiculo):
    def __init__(self, id_veiculo: int, velocidade_maxima: float, cor: str, matricula: str):
        super().__init__(id_veiculo, velocidade_maxima, cor, matricula)
        self.categoria = 'Ligeiros'
    @classmethod


    def manualInsert(cls):
        while True:
            try:
                id_veiculo = int(input("Digite o ID do veículo: "))
                break
            except ValueError:
                print("Valor inválido para o ID. Por favor, insira um número inteiro.")

        while True:
            try:
                velocidade_maxima = float(input("Digite a velocidade máxima do veículo (km/h): "))
                break
            except ValueError:
                print("Valor invalido para a velocidade. Por favor, insira um número.")

       
        cor = input("Digite a cor do veiculo: ")
        matricula = input("Digite a matricula do veiculo: ")
        print("criado com sucesso!!")
        return cls(id_veiculo, velocidade_maxima, cor, matricula)
