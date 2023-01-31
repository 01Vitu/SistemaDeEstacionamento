# Classe para representar o veículo
class Veiculo:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

# Classe para representar o estacionamento
class Estacionamento:
    def __init__(self):
        self.veiculos_estacionados = []

    # Método para adicionar um veículo ao estacionamento
    def adicionar_veiculo(self, veiculo):
        self.veiculos_estacionados.append(veiculo)

    # Método para remover um veículo do estacionamento
    def remover_veiculo(self, veiculo):
        self.veiculos_estacionados.remove(veiculo)

    # Método para listar os veículos estacionados
    def listar_veiculos(self):
        for i, veiculo in enumerate(self.veiculos_estacionados):
            print(f"{i+1}: Placa {veiculo.placa}, Modelo {veiculo.modelo}")

# Criando o objeto estacionamento
estacionamento = Estacionamento()

# Loop para interação com o usuário
while True:
    opcao = input("Escolha a opção desejada (1 - Adicionar veículo, 2 - Remover veículo, 3 - Listar veículos, 4 - Sair): ")

    if opcao == "1":
        placa = input("Digite a placa do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        veiculo = Veiculo(placa, modelo)
        estacionamento.adicionar_veiculo(veiculo)
        print("Veículo adicionado com sucesso!")

    elif opcao == "2":
        placa = input("Digite a placa do veículo a ser removido: ")
        for veiculo in estacionamento.veiculos_estacionados:
            if veiculo.placa == placa:
                estacionamento.remover_veiculo(veiculo)
                print("Veículo removido com sucesso!")
                break
        else:
            print("Veículo não encontrado!")

    elif opcao == "3":
        estacionamento.listar_veiculos()

    elif opcao == "4":
        break

