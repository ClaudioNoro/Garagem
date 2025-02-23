# Veiculo.py
class Veiculo:
    def __init__(self, id_veiculo, velocidade_maxima, cor, matricula):
        self.id_veiculo = id_veiculo
        self.velocidade_maxima = velocidade_maxima
        self.cor = cor
        self.matricula = matricula
        self.categoria = None  

    def __str__(self):
       return (f"Veículo [ID: {self.id_veiculo}, Categoria: {self.categoria}, "
                f"Cor: {self.cor}, Matrícula: {self.matricula}, "
                f"Velocidade Máxima: {self.velocidade_maxima} km/h]")
