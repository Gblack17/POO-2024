from enum import Enum
from datetime import date, timedelta, datetime
import re

# Dados iniciais
dados_pessoa = [
    {"cpf_pessoa": "12345678910", "nome_pessoa": "João Silva", "data_nascimento": "10/04/1990", "crm_pessoa": None},
    {"cpf_pessoa": "10987654321", "nome_pessoa": "Maria Souza", "data_nascimento": "20/08/1985", "crm_pessoa": None},
    {"cpf_pessoa": "112233445566", "nome_pessoa": "Chico Buarque", "data_nascimento": "19/07/1944", "crm_pessoa": "345621"}
]

class StatusPrescricao(Enum):
    VÁLIDA = 1
    INVÁLIDA = 2

class StatusMedicamento(Enum):
    DISPONÍVEL = 1
    INDISPONÍVEL = 2

class Pessoa:
    def __init__(self, nome_pessoa, cpf_pessoa, crm_pessoa=None):
        self.nome_pessoa = nome_pessoa
        self.cpf_pessoa = cpf_pessoa
        self.crm_pessoa = crm_pessoa

class Prescricao:
    def __init__(self, paciente, medicamento, data_prescricao):
        self.paciente = paciente
        self.medicamento = medicamento
        self.data_prescricao = data_prescricao
        self.status = StatusPrescricao.VÁLIDA

class Medicamento:
    def __init__(self, nome):
        self.nome = nome
        self.status = StatusMedicamento.INDISPONÍVEL

    def __str__(self):
        return f"Medicamento: {self.nome}, Status: {self.status.name}"

class MedicamentoEstoque:
    def __init__(self, medicamento, quantidade):
        self.medicamento = medicamento
        self.quantidade = quantidade

class Farmacia:
    def __init__(self, estoque):
        self.estoque = estoque

    def verificar_estoque(self, medicamento_nome):
        for item in self.estoque:
            if item.medicamento.nome == medicamento_nome:
                return item
        return None

    def vender_medicamento(self, prescricao):
        if prescricao.status != StatusPrescricao.VÁLIDA:
            print("Prescrição inválida. Não é possível dispensar o medicamento.")
            return

        item_estoque = self.verificar_estoque(prescricao.medicamento.nome)
        if not item_estoque or item_estoque.quantidade == 0:
            print("Medicamento indisponível no estoque.")
        else:
            item_estoque.quantidade -= 1
            print(f"Medicamento {prescricao.medicamento.nome} dispensado. Estoque atualizado.")

# Validações
def validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    return True

def validar_prescricao(prescricao, dados_pessoa):
    """
    Valida a prescrição:
    - Verifica se o CPF e o nome do paciente correspondem aos registros.
    - Verifica se a data da prescrição está dentro do prazo permitido (30 dias).
    """
    # Verifica se o CPF e o nome correspondem
    for pessoa in dados_pessoa:
        if pessoa["cpf_pessoa"] == prescricao.paciente.cpf_pessoa and pessoa["nome_pessoa"] == prescricao.paciente.nome_pessoa:
            break
    else:
        prescricao.status = StatusPrescricao.INVÁLIDA
        print("CPF ou nome do paciente não correspondem aos dados registrados.")
        return False

    # Verifica se a data está dentro do prazo
    hoje = date.today()
    limite_inferior = hoje - timedelta(days=30)  # Limite de 30 dias atrás
    if not (limite_inferior <= prescricao.data_prescricao <= hoje):
        prescricao.status = StatusPrescricao.INVÁLIDA
        print(f"Prescrição fora do período válido. Só são aceitas prescrições entre {limite_inferior} e {hoje}.")
        return False

    return True

# Estoque inicial
estoque = [
    MedicamentoEstoque(Medicamento("Dipirona"), 50),
    MedicamentoEstoque(Medicamento("Azitromicina"), 10)
]

# Main
def main():
    farmacia = Farmacia(estoque)

    print("Bem-vindo ao sistema de dispensação de medicamentos!")
    while True:
        print("\nEscolha uma ação:")
        print("1. Apresentar prescrição")
        print("2. Sair")

        escolha = input("> ")

        if escolha == "1":
            # Entrada dos dados da prescrição
            nome_paciente = input("Nome do paciente: ")
            cpf_paciente = input("CPF do paciente: ")
            medicamento_nome = input("Nome do medicamento: ")
            data_prescricao_str = input("Data da prescrição (DD/MM/AAAA): ")

            # Validação de entrada
            try:
                data_prescricao = datetime.strptime(data_prescricao_str, "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")
                continue

            if not validar_cpf(cpf_paciente):
                print("CPF inválido. Verifique os dados e tente novamente.")
                continue

            paciente = Pessoa(nome_paciente, cpf_paciente)
            medicamento = Medicamento(medicamento_nome)
            prescricao = Prescricao(paciente, medicamento, data_prescricao)

            # Validação da prescrição
            if validar_prescricao(prescricao, dados_pessoa):
                print("Prescrição válida. Verificando estoque...")
                item_estoque = farmacia.verificar_estoque(medicamento_nome)
                if item_estoque and item_estoque.quantidade > 0:
                    farmacia.vender_medicamento(prescricao)
                else:
                    print("Medicamento indisponível no estoque.")
            else:
                print("Prescrição inválida.")

        elif escolha == "2":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
