from exceptions import (DescricaoEmBrancoException,
                        ValorDeducaoInvalidoException,
                        ValorRendimentoInvalidoException,
                        ValorPensaoAlimenticiaInvalidoException,
                        NomeEmBrancoException)


class SimuladorIRPF:
    total_rendimentos = 0.0
    total_deducoes = 0.0
    total_dependentes = 0
    rendimentos = []
    deducoes = []
    pensoes_alimenticias = []
    contribuicoes_previdenciarias = []
    dependentes = []

    def cadastrar_rendimento(self, descricao: str, valor: float):
        if descricao.strip() == "":
            raise DescricaoEmBrancoException

        if valor <= 0:
            raise ValorRendimentoInvalidoException

    def cadastrar_deducao(self, descricao: str, valor: float):
        if descricao.strip() == "":
            raise DescricaoEmBrancoException

        if valor <= 0:
            raise ValorDeducaoInvalidoException

    def cadastrar_contribuicao_oficial(self, descricao: str, valor: float):
        self.cadastrar_deducao(descricao, valor)

    def cadastrar_pensao_alimenticia(self, valor: float):
        if valor <= 0:
            raise ValorPensaoAlimenticiaInvalidoException

        self.pensoes_alimenticias.append(valor)
        self.total_deducoes += valor

    def cadastrar_dependente(self, nome: str, data_nascimento: str):
        if nome.strip() == "":
            raise NomeEmBrancoException

        dependente = {"nome": nome, "data_nascimento": data_nascimento}

        self.dependentes.append(dependente)
        self.total_deducoes += 189.59
        self.total_dependentes += 1

    def calcular_primeira_faixa(self) -> float:
        return 0.0

    def calcular_segunda_faixa(self) -> float:
        return 0.0

    def calcular_terceira_faixa(self) -> float:
        return 0.0

    def calcular_quarta_faixa(self) -> float:
        return 0.0

    def calcular_quinta_faixa(self) -> float:
        return 0.0

    def calcular_total_imposto(self):
        total = self.calcular_primeira_faixa()
        total += self.calcular_segunda_faixa()
        total += self.calcular_terceira_faixa()
        total += self.calcular_quarta_faixa()
        total += self.calcular_quinta_faixa()

        return total

    def calcular_aliquota_efetiva(self) -> float:
        return 0;
