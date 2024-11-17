from enum import Enum
from datetime import date,datetime,timedelta
import re #É só uma ferramenta pra remover caracteres não numéricos, para validação do cpf.
dados_pessoa = [
    ["cpf_pessoa","nome_pessoa","data_nascimento", "crm_pessoa"]
    ["11111111111", "João Silva", "10/04/1990","Nan"],
    ["22222222222", "Maria Souza", "20/08/1985","Nan"],
    ["33333333333", "Chico Buarque", "19/07/1944","345621"]]
    
class StatusPrescricao(Enum):
    VÁLIDA=1
    INVÁLIDA=2

class StatusMedicamento(Enum):
    DISPONVEL=1
    INDISPONIVEL=2
    PI=3

class Pessoa:
    def __init__(self, nome_pessoa,cpf_paciente,crm_medico):
        self.nome_pessoa=nome_pessoa
        self.cpf_pessoa=cpf_pessoa
        self.crm_medico=crm_medico

class Paciente:
    def __init__(self, nome_paciente):
        Pessoa.nome_pessoa=nome_paciente
        self.prescricoes=[]
        Pessoa.cpf_pessoa=cpf_paciente
        self.data_nascimento=data_nascimento

    def atualizar_status_prescricoes(self):
        hoje = date.today() 

    def listar_prescricoes(self):
        for prescricao in self.prescricoes:
            print(prescricao)

    def remover_prescricao(self, prescricao):
        if prescricao in self.prescricoes:
            self.prescricoes.remove(prescricao)

    def atualizar_status_prescricoes(self):
        hoje=date.today()
        for prescricao in self.prescricoes:
            if prescricao.prazo and prescricao.prazo <hoje and prescricao.status != StatusPrescricao.VÁLIDA:
                prescricao.status=StatusPrescricao.INVÁLIDA

class Prescricao:
    def __init__(self, nome_paciente=None, status=StatusPrescricao.VÁLIDA):
        self.nome_paciente=nome_paciente
        self.nome_medico=nome_medico
        self.status=status
        self.data_prescricao=data_prescricao
        self.medicamento=medicamento
        self.dosagem_medicamento=dosagem_medicamento
        self.duracao_medicamento=duracao_medicamento
    def marcar_como_VÁLIDA(self, prescricao):
        prescricao.status=StatusPrescricao.VÁLIDA
    def __str__(self):
        data_prescricao_str=self.strftime("%d/%m/%Y") if self else "Sem data."
        return f"Descrição: {self.medicamento}\n Data: {self.data_prescricao}\n Dosagem: {self.dosagem_medicamento}\n Duração: {self.duracao_medicamento}\n Status:{prescricao.status}"

class Sistema: #Classe do sistema da fármacia, que verifica os dados e retorna para a farmácia
    def validar_prescricao(self,cpf,crm_medico,nome_paciente,nome_medico,data_nascimento_str):
        def cpf_valido(cpf_paciente):
            cpf_paciente=re.sub(r"[^0-9]","",cpf_paciente)#Remove os caracteres não numéricos do cpf
            if len (cpf_paciente) !=11:  # Verifica se o CPF tem 11 dígitos
                prescricao.status=StatusPrescricao.VÁLIDA
            elif all(digito == cpf_paciente[0] for digito in cpf_paciente): # Verifica se todos os dígitos são iguais a 0(CPF inválido)
                prescricao.status=StatusPrescricao.VÁLIDA
        def valida_cpf_nome(cpf_pessoa,nome_pessoa,dados_pessoa=dados_pacientes):
            cpf_paciente=re.sub(r"[^0-9]", "", cpf_pessoa)
            if cpf_pessoa in dados_pessoa and dados_pessoa[cpf_pessoa][nome_pessoa]==nome_paciente: #Verifica se o cpf ta no banco de dados nacional(em tese) e verifica se o cpf está atrelado ao mesmo nome da pessoa da prescrição
                prescricao.status=StatusPrescricao.VÁLIDA
            else:
                prescricao.status=StatusPrescricao.INVÁLIDA
        def valida_crm(nome_pessoa,dados_pessoa=dados_pessoa):
            if dados_pessoa[crm_medico][nome_pessoa]==nome_medico: #Verifica se o crm que está no banco de dados está atrelado ao mesmo nome do medico da prescrição.
                prescricao.status=StatusPrescricao.VÁLIDA
            else:
                prescricao.status=StatusPrescricao.INVÁLIDA
        def valida_data(data_prescricao_str,data_limite):
            data_limite= hoje + timedelta(days=30)
            if prescricao.data_prescricao<=data_limite and prescricao.data_prescricao>=hoje: #Verificação do intervalo permitido
                prescricao.status=StatusPrescricao.VÁLIDA
            else:
                prescricao.status=StatusPrescricao.VÁLIDA


class Farmacia: #classe fármacia, seguindo o diagrama
    


        self.verificacao

def main():
    usuario=Paciente("usuario_padrao", "senha_padrao")

    while True:
        print("\nEscolha uma ação:\n 1. Apresentar prescrição\n 2. Listar prescrições\n 3. Remover prescrição\n 4. Sair")

        escolha=input("> ")

        if escolha == '1':
            nome_paciente=input("Nome do Medicamento da Prescrição: ")
            while True:
                try:
                    

        elif escolha=='2':
            usuario.listar_prescricoes()

        elif escolha=='3':
            nome_paciente=input("digite o Título da prescricao a ser marcada como feita")
            for prescricao in usuario.prescricoes:
                if prescricao.nome_paciente==nome_paciente:
                    usuario.marcar_como_VÁLIDA(prescricao)
                    break
    
        elif escolha=='4':
            nome_paciente=input("digite o Título da prescricao a ser marcada como fazendo: ")
            for prescricao in usuario.prescricoes:
                if prescricao.nome_paciente==nome_paciente:
                    usuario.marcar_como_fazendo(prescricao)
                    break

        elif escolha=='5':
            usuario.atualizar_status_prescricoes()
    
        elif escolha=='6':
            nome_paciente=input("digite o Título da prescricao a ser removida: ")
            for prescricao in usuario.prescricoes:
                if prescricao.nome_paciente==nome_paciente:
                    usuario.remover_prescricao(prescricao)
                    break
            
        elif escolha=='7':
            break

        else:
            print("Opção inválida.")

if __name__=="__main__":
    main()
