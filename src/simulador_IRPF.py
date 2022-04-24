from typing import Union

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

    def cadastrar(self, tipo: str, valor: float, descricao: Union[str, None] = None):
        if descricao and descricao.strip() == "":
            raise DescricaoEmBrancoException

        if valor <= 0:
            if tipo == 'rendimento':
                raise ValorRendimentoInvalidoException
            if tipo == 'deducao':
                raise ValorDeducaoInvalidoException

        if tipo == "rendimento":
            if descricao:
                rendimento = {"descricao": descricao, "valor": valor}
                self.rendimentos.append(rendimento)
            self.total_rendimentos += valor

        if tipo == "deducao":
            if descricao:
                deducao = {"descricao": descricao, "valor": valor}
                self.deducoes.append(deducao)
            self.total_deducoes += valor

    def cadastrar_rendimento(self, valor: float, descricao: Union[str, None] = None):
        self.cadastrar(tipo='rendimento', valor=valor, descricao=descricao)

    def cadastrar_deducao(self, valor: float, descricao: Union[str, None] = None):
        self.cadastrar(tipo='deducao', valor=valor, descricao=descricao)

    def cadastrar_contribuicao_oficial(self, descricao: str, valor: float):
        self.cadastrar_deducao(valor, descricao)

    def cadastrar_pensao_alimenticia(self, valor: float):
        if valor <= 0:
            raise ValorPensaoAlimenticiaInvalidoException

        self.pensoes_alimenticias.append(valor)
        self.cadastrar_deducao(valor=valor)

    def cadastrar_dependente(self, nome: str, data_nascimento: str):
        if nome.strip() == "":
            raise NomeEmBrancoException

        dependente = {"nome": nome, "data_nascimento": data_nascimento}
        self.total_dependentes += 1
        self.dependentes.append(dependente)
        self.cadastrar_deducao(valor=189.59)

    def calcular_primeira_faixa(self) -> float:
        return 0.0

    def calcular_segunda_faixa(self) -> float:
        base = self.total_rendimentos - self.total_deducoes
        base_segunda_faixa = base - 1903.98

        if base_segunda_faixa <= 0:
            return 0

        if base_segunda_faixa >= 922.67:
            return (7.5/100) * 922.67

        return base_segunda_faixa * (7.5/100)

    def calcular_terceira_faixa(self) -> float:
        base = self.total_rendimentos - self.total_deducoes
        base_terceira_faixa = base - (1903.98 + 922.67)

        if base_terceira_faixa <= 0:
            return 0

        if base_terceira_faixa >= 924.40:
            return (15 / 100) * 924.40

        return base_terceira_faixa * (15 / 100)

    def calcular_quarta_faixa(self) -> float:
        base = self.total_rendimentos - self.total_deducoes
        base_quarta_faixa = base - (1903.98 + 922.67 + 924.40)

        if base_quarta_faixa <= 0:
            return 0

        if base_quarta_faixa >= 913.63:
            return (22.5 / 100) * 913.63

        return base_quarta_faixa * (22.5 / 100)

    def calcular_quinta_faixa(self) -> float:
        base = self.total_rendimentos - self.total_deducoes
        base_quinta_faixa = base - (1903.98 + 922.67 + 924.40 + 913.63)

        if base_quinta_faixa <= 0:
            return 0

        return base_quinta_faixa * (27.5 / 100)

    def calcular_total_imposto(self):
        total = self.calcular_primeira_faixa()
        total += self.calcular_segunda_faixa()
        total += self.calcular_terceira_faixa()
        total += self.calcular_quarta_faixa()
        total += self.calcular_quinta_faixa()

        return total

    def calcular_aliquota_efetiva(self) -> float:
        return round(100 * (self.calcular_total_imposto()/self.total_rendimentos),2)