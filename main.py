# main.py
import pandas as pd
from Veiculo import Veiculo
from Pesados import Pesados
from Ligeiros import Ligeiros
carrosNaGaragem = []
def ler_dados_veiculos(arquivo: str):
    """
    Lê um arquivo Excel com dados de veículos e retorna uma lista
    'carrosNaGaragem' com instâncias de Pesados ou Ligeiros, conforme a categoria.
    """
    df = pd.read_excel(arquivo)
    #dataframe pandas ->estudar 
    
    for _, row in df.iterrows():
        id_veiculo = row["ID"]
        categoria = row["Categoria"].strip().lower()
        cor = row["Cor"]
        matricula = row["Matricula"]
        velocidade_maxima = row["Velocidade_max"]

        if categoria == "pesados":
            # Obtém o valor da carga máxima
            carga_max = row["CargaMax"]
            if pd.isna(carga_max):
                print(f"CargaMax ausente para veículo ID {id_veiculo}. Pulando este registro.")
                continue
            try:
                # Converte para string e substitui vírgula por ponto (para casos como '3750,5')
                carga_max = float(str(carga_max).replace(",", "."))
            except ValueError:
                print(f"Valor inválido para CargaMax no veículo ID {id_veiculo}.")
                continue

            veiculo = Pesados(id_veiculo, velocidade_maxima, cor, matricula, carga_max)
        elif categoria == "ligeiros":
            veiculo = Ligeiros(id_veiculo, velocidade_maxima, cor, matricula)
        else:
            print(f"Categoria desconhecida para o veículo ID {id_veiculo}: {row['Categoria']}")
            continue
        carrosNaGaragem.append(veiculo)
        print(veiculo)
    
    return carrosNaGaragem


def salvar_dados_excel(arquivo: str):
    """
    Lê os dados da lista global 'carrosNaGaragem' e exporta para um arquivo Excel.
    O Excel conterá as colunas: ID, Categoria, Cor, Matricula, Velocidade_max e CargaMax.
    Para veículos do tipo Ligeiros (que não possuem carga máxima), o campo 'CargaMax' ficará vazio.
    """
    dados = []
    for veiculo in carrosNaGaragem:
        item = {
            "ID": veiculo.id_veiculo,
            "Categoria": veiculo.categoria,
            "Cor": veiculo.cor,
            "Matricula": veiculo.matricula,
            "Velocidade_max": veiculo.velocidade_maxima,
        }
        # Se o veículo tiver o atributo 'CargaMax' (ou seja, for um Pesados), adiciona-o; caso contrário, deixa vazio.
        if hasattr(veiculo, "CargaMax"):
            item["CargaMax"] = veiculo.CargaMax
        else:
            item["CargaMax"] = ""
        dados.append(item)
    
    df = pd.DataFrame(dados)
    #Converte a lista de dicionários dados em um DataFrame do pandas. Cada dicionário se transforma em uma linha, e as chaves dos dicionários se tornam os nomes das colunas.
    df.to_excel(arquivo, index=False)
    print(f"Arquivo '{arquivo}' salvo com sucesso!")


def addVeiculo():
    print("1 - Ligeiro  2 - Pesado  0 - Retornar")
    tipo = input("Selecione o tipo de veículo: ")
    
    match tipo:
        case "0":
            print("Retornando ao menu...")
        case "1":
            print("Criando veículo Ligeiro...")
            novoLigeiro= Ligeiros.manualInsert()
            carrosNaGaragem.append(novoLigeiro)
        case "2":
            print("Criando veículo Pesado...")
            novoPesado=Pesados.manualInsert()
            carrosNaGaragem.append(novoPesado)
        case _:
            print("Opção inválida")

def ListarVeiculos():
    for item in carrosNaGaragem:
        print(item)

def menu():
    print("\n====Menu da Garagem=====")
    print("1 - Adicionar Veiculo")
    print("2 - Listar Veiculos na garagem")
    print("3 - Remover veiculo da garagem")
    print("4 - Salvar dados xlsx")
    print("0 - Sair")

def main():
    ler_dados_veiculos("dados_veiculos.xlsx")
    while True:
        menu()
        opcao= input("escolher opcao: ")
        match opcao:
            case "0":
                print("Encerrando o programa")
                break
            case "1":
                addVeiculo()
            case "2":
                ListarVeiculos()
            case "3":
                ##
                break
            case "4":
                salvar_dados_excel("dados_veiculos.xlsx")
            case _:
                print("opcao invalida! tente novamente")


if __name__ == "__main__":
    main()