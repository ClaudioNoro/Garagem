# Pesados.py
from Veiculo import Veiculo

class Pesados(Veiculo):
    def __init__(self, id_veiculo: int, velocidade_maxima: float, cor: str, matricula: str, carga_max: float):
        super().__init__(id_veiculo, velocidade_maxima, cor, matricula)
        self.categoria = 'Pesados'
        self.CargaMax = carga_max

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
                print("Valor inválido para a velocidade. Por favor, insira um número.")

        cor = input("Digite a cor do veículo: ")
        matricula = input("Digite a matricula do veiculo pesado: ")

        while True:
            try:
                carga_max = float(input("Digite a carga máxima do veículo: "))
                break
            except ValueError:
                print("Valor invalido para a carga maxima. insira um numero.")
        print("criado com sucesso!!")
        return cls(id_veiculo, velocidade_maxima, cor, matricula, carga_max)
    


    def __str__(self):
           return (f"Veículo [ID: {self.id_veiculo}, Categoria: {self.categoria}, "
                    f"Cor: {self.cor}, Matrícula: {self.matricula}, "
                    f"Velocidade Máxima: {self.velocidade_maxima} km/h,"
                    f"Carga Maxima:{self.CargaMax}KG]")